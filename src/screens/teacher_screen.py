import streamlit as st
from src.ui.base_layout import style_background_dashboard,style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.database.db import check_teacher_exists, create_teacher ,teacher_login,get_teacher_subjects,get_attendance_for_teacher
from src.components.dialogue_create_subject import create_subject_dialogue
from src.components.subject_card import subject_card
from src.components.dialogue_share_subject import share_subject_dialog
from src.components.dialog_add_photo import add_photos_dialog
import numpy as np
from src.pipeline.face_pipeline import predict_attendance
from src.database.config import supabase
from datetime import datetime
from src.components.dialog_attendance_results import show_attendance_result
import pandas as pd
from src.components.dialog_voice_attendance import voice_attendance_dialog




def teacher_screen():
    style_background_dashboard()
    style_base_layout()
    if "teacher_data" in st.session_state:
        teacher_dashboard()
    elif "teacher_login_type" not in st.session_state or st.session_state.teacher_login_type=="login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type=="register":
        teacher_screen_register()

def teacher_dashboard():
    teacher_data=st.session_state.teacher_data
    col1,col2=st.columns(2,vertical_alignment="center",gap="xlarge")
    with col1:
        header_dashboard()
    with col2:
        st.subheader(f""" Welcome,{teacher_data['name']}""")
        if st.button("Logout",type="tertiary",key="loginbackbtn",width="stretch",shortcut="control+backspace"):
            st.session_state["is_logged_in"]=False
            del st.session_state.teacher_data
            st.rerun()
    st.space()
    if "current_teacher_tab" not in st.session_state:
        st.session_state.current_teacher_tab='take_attendance'
    tab1,tab2,tab3=st.columns(3)
    with tab1:
        type1="primary" if st.session_state.current_teacher_tab=='take_attendance'else"tertiary"
        if st.button('Take Attendance',type=type1,width='stretch',icon=':material/ar_on_you:'):
            st.session_state.current_teacher_tab='take_attendance'
            st.rerun()
    with tab2:
        type2="primary" if st.session_state.current_teacher_tab=='manage_subjects'else"tertiary"
        if st.button('Manage Subject',type=type2,width='stretch',icon=':material/ar_on_you:'):
            st.session_state.current_teacher_tab='manage_subjects'
            st.rerun()
    with tab3:
        type3="primary" if st.session_state.current_teacher_tab=='attendance_records'else"tertiary"
        if st.button('Attendance Records',type=type3,width='stretch',icon=':material/ar_on_you:'):
            st.session_state.current_teacher_tab='attendance_records'
            st.rerun()
    st.divider()
    if st.session_state.current_teacher_tab=='take_attendance':
        teacher_tab_take_attendance()
    if st.session_state.current_teacher_tab=='manage_subjects':
        teacher_tab_manage_subjects()
    if st.session_state.current_teacher_tab=='attendance_records':
        teacher_tab_attendance_records()

    footer_dashboard()

def teacher_tab_take_attendance():
    teacher_id=st.session_state.teacher_data['teacher_id']
    st.header('Take AI Attendance')

    if 'attendance_images' not in st.session_state:
        st.session_state.attendance_images=[]

    subjects=get_teacher_subjects(teacher_id)
    if not subjects:
        st.warning("You haven't created any subjects yet! Please create one to begin!")
        return
    subject_options={f"{s['name']}-{s['subject_code']}":s['subject_id'] for s in subjects}
    col1,col2=st.columns([3,1],vertical_alignment='bottom')
    with col1:
        selected_subject_label=st.selectbox('Select Subject',options=list(subject_options.keys()))
    with col2:
        if st.button("Add Photos",type="primary",icon=":material/photo_prints:",width="stretch"):
            add_photos_dialog()

    selected_subject_id=subject_options[selected_subject_label]
    st.divider()
    if st.session_state.attendance_images:
        st.header('Added Photos')
        gallery_cols=st.columns(4)

        for idx,img in enumerate(st.session_state.attendance_images):
            with gallery_cols[idx%4]:
                st.image(img,width='stretch',caption=f'photo {idx+1}')
    c1,c2,c3=st.columns(3)
    has_photos=bool(st.session_state.attendance_images)
    with c1:
        if st.button('Clear all photos',width='stretch',type='tertiary',icon=':material/delete:',disabled=not has_photos):
            st.session_state.attendance_images=[]
            st.rerun()
    with c2:
        if st.button('Run Face Analysis',width='stretch',type='secondary',icon=':material/analytics:',disabled=not has_photos):
            with st.spinner("Deep Scanning Classroom Photos..."):
                all_detected_id={}

                for idx,img in enumerate(st.session_state.attendance_images):
                    img_np=np.array(img.convert('RGB'))

                    detected,_,_=predict_attendance(img_np)

                    if detected:
                        for sid in detected.keys():
                            student_id=int(sid)

                            all_detected_id.setdefault(student_id,[]).append(f"photo{idx+1}")
                enrolled_res=supabase.table('subject_students').select("*,students(*)").eq('subject_id',selected_subject_id).execute()
                enrolled_students=enrolled_res.data

                if not enrolled_students:
                    st.warning('No students enrolled in this course')
                else:
                    results,attendance_to_log=[],[]
                    current_timestamp=datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
                    for node in enrolled_students:
                        student=node['students']
                        sources=all_detected_id.get(int(student['student_id']),[])
                        is_present=len(sources)>0
                        results.append({
                            "Name":student['name'],
                            "ID":student['student_id'],
                            "sources":",".join(sources) if is_present else "_",
                            "Status":"✅ Present" if is_present else "❌Absent"
                        })
                        attendance_to_log.append({
                            'student_id':student['student_id'],
                            'subject_id':selected_subject_id,
                            'timestamp':current_timestamp,
                            'is_present':bool(is_present)
                        })
            show_attendance_result(pd.DataFrame(results),attendance_to_log)
    with c3:
        if st.button('Use Voice Attendance',type='primary',width='stretch',icon=":material/mic:"):
            voice_attendance_dialog(selected_subject_id)
    if st.session_state.get('voice_attendance_results'):
        st.divider()
        df_results,logs=st.session_state.voice_attendance_results
        show_attendance_result(df_results,logs)


def teacher_tab_manage_subjects():
    teacher_id=st.session_state.teacher_data["teacher_id"]
    col1,col2=st.columns(2)
    with col1:
        st.header("Manage Subjects",width="stretch")
    with col2:
        if st.button("Create New Subject",width='content'):
            create_subject_dialogue(teacher_id)

    #list  all subjects
    subjects=get_teacher_subjects(teacher_id)
    if subjects:
        for sub in subjects:
            stats=[
                ("👩🏻‍🎓"," students", sub['total_students']),
                ("⏰"," classes", sub['total_classes']),

            ]
             
            def share_btn():
                if st.button(f"share Code: {sub['name']}",key=f"share_{sub['subject_id']}",icon=":material/share:"):
                    share_subject_dialog(sub['name'],sub['subject_code'])
                st.space()

            subject_card(
                name=sub['name'],
                code=sub['subject_code'],
                section=sub['section'],
                stats=stats,
                footer_callback=share_btn
            )
    else:
        st.info("NO SUBJECTS FOUND CREATE ONE ABOVE")


def teacher_tab_attendance_records():
    st.header("Attendance records")
    teacher_id=st.session_state.teacher_data['teacher_id']
    records=get_attendance_for_teacher(teacher_id)

    if not records:
        return
    data=[]
    for r in records:
        ts=r.get('timestamp')
        data.append({
            "ts_group":ts.split(".")[0] if ts else None,
            "Time":datetime.fromisoformat(ts).strftime("%Y-%m-%d %I:%M %p")if ts else "NA",
            "subjects":r['subjects']['name'],
            "subject code":r['subjects']['subject_code'],
            "is_present":bool(r.get('is_present',False))
        })
    
    df=pd.DataFrame(data)

    summary=(
        df.groupby(['ts_group','Time','subjects','subject code'])
        .agg(
            present_count=('is_present','sum'),
            Total_count=('is_present','count')

        ).reset_index()
    )
    summary['Attendance stats']=(
        "✅"+summary['present_count'].astype(str)+"/"+summary['Total_count'].astype(str)+'students'
    )

    display_df=(summary.sort_values(by="ts_group",ascending=False)
                [['Time','subjects','subject code','Attendance stats']]
                )
    st.dataframe(display_df,width='stretch',hide_index=True)

def login_teacher(username,password):
    if not username or not password:
        return False
    teacher=teacher_login(username,password)
    if teacher:
        st.session_state.user_role="teacher"
        st.session_state.teacher_data=teacher
        st.session_state.is_logged_in=True
        return True
    return False


def teacher_screen_login():
    col1,col2=st.columns(2,vertical_alignment="center",gap="xlarge")
    with col1:
        header_dashboard()
    with col2:
        if st.button("Go back to Home",type="tertiary",key="loginbackbtn",width="stretch",shortcut="control+backspace"):
            st.session_state["login_type"]=None
            st.rerun()
    st.header("LOGIN USING PASSWORD",text_alignment="center")
    st.space()
    teacher_username=st.text_input("Enter username",placeholder='Username')
    teacher_pass=st.text_input("Enter password",placeholder="Enter password",type="password")
    st.space()
    btn1,btn2=st.columns(2)
    with btn1:
        if st.button("Login",icon=":material/passkey:",shortcut="enter",width="stretch"):
            if login_teacher(teacher_username,teacher_pass):
                st.toast("Welcome back!",icon="👋")
                import time
                time.sleep(1)
                st.rerun()
            else:
                st.error("Invalid username and password combo")
    with btn2:
        if st.button("Register Instead",type="primary",icon=":material/passkey:",width="stretch"):
            st.session_state.teacher_login_type="register"
    footer_dashboard()

def register_teacher(teacher_username,teacher_name,teacher_pass,teacher_pass_confirm):
    if not teacher_username or not teacher_name or not teacher_pass:
        return False ,"All Fields are required!"
    if check_teacher_exists(teacher_username):
        return False,"username already taken"
    if teacher_pass != teacher_pass_confirm:
        return False,"password doesn't match"
    try:
        create_teacher(teacher_username,teacher_pass,teacher_name)
        return True,"sucessfully Created! Login Now"
    except Exception as e:
        return False,"unexpected error!"
            
def teacher_screen_register():
   
    col1,col2=st.columns(2,vertical_alignment="center",gap="xlarge")
    with col1:
        header_dashboard()
    with col2:
        if st.button("Go back to Home",type="tertiary",key="loginbackbtn",width="stretch",shortcut="control+backspace"):
            st.session_state["login_type"]=None
            st.rerun()
    st.header("Register your Teacher Profile",text_alignment="center")
   
    teacher_username=st.text_input("Enter username",placeholder='Username')
    teacher_name=st.text_input("Enter name",placeholder='Name')
    teacher_pass=st.text_input("Enter password",placeholder="Enter password",type="password")
    teacher_pass_confirm=st.text_input("Confirm password",placeholder="Confirm password",type="password")
    btn1,btn2=st.columns(2)
    with btn1:
        if st.button("Login Instead",icon=":material/passkey:",shortcut="Enter",width="stretch"):
            st.session_state.teacher_login_type="login"
    with btn2:
        if st.button("Register Now",type="primary",icon=":material/passkey:",width="stretch"):
            success,message=register_teacher(teacher_username,teacher_name,teacher_pass,teacher_pass_confirm)
            if success:
                st.success(message)
                import time
                time.sleep(2)
                st.session_state.teacher_login_type="login"
                st.rerun()
            else:
                st.error(message)

            
    footer_dashboard()