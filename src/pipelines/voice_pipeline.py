import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase
import time


from src.database.db import create_attendance

def get_voice_embedding(audio_source):
    """Extract a normalized MFCC feature vector from audio input."""
    import io
    import librosa
    import numpy as np

    if isinstance(audio_source, bytes):
        audio_source = io.BytesIO(audio_source)

    audio, sample_rate = librosa.load(audio_source, sr=16000, mono=True)
    if audio.size == 0:
        raise ValueError('Audio source is empty.')

    features = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=20)
    embedding = np.concatenate((features.mean(axis=1), features.std(axis=1)))
    norm = np.linalg.norm(embedding)
    return embedding / norm if norm else embedding


def show_attendance_result(df, logs):
    st.write('Please review attendance before confirming.')
    st.dataframe(df, hide_index=True, width='stretch')

    col1, col2 = st.columns(2)

    with col1:
        if st.button('Discard', width='stretch'):
            st.session_state.voice_attendance_results = None
            st.session_state.attendance_images = []
            st.rerun()

    with col2:
        if st.button('Confirm & Save', width='stretch', type='primary'):
            try:
                create_attendance(logs)
                st.toast("Attendance taken")
                st.session_state.attendance_images = []
                st.session_state.voice_attendance_results = None
                st.rerun()
            except Exception as e:
                st.error('Sync failed!')



@st.dialog("Attendance Reports")
def attendance_result_dialog(df, logs):
    show_attendance_result(df, logs)


