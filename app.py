import streamlit as st
from moviepy.editor import *
import pytube 
st.title("MP4 to MP3 Converter")
st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://wallpaperaccess.com/full/215123.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
mp4_url = st.text_input("Enter MP4 URL:")
if "youtube.com" in mp4_url or "youtu.be" in mp4_url:
    try:
        # Create a YouTube object using the video URL
        yt = pytube.YouTube(mp4_url)
        
        # Display the video details to the user
        st.write("Title:", yt.title)
        st.write("Duration:", yt.length, "seconds")
        st.write("Views:", yt.views)
        
        # Add a download button for the video in MP3 format
        if st.button("Convert to MP3"):
            try:
                with st.spinner("Converting..."):
                    stream = yt.streams.filter(only_audio=True).first()
                    # Convert the audio to MP3 format using moviepy.editor
                    audio = AudioFileClip(stream.url)
                    audio.write_audiofile("output.mp3")
                    
                    # Display a success message to the user
                st.success("Conversion complete!")
            except:
                st.error("Conversion failed.")
            with open("output.mp3", "rb") as f:
                byte_content = f.read()
                st.download_button(
                    label="Download MP3",
                    data=byte_content,
                    file_name="output.mp3",
                    mime="audio/mpeg",
                )
        
    except:
        # Display an error message if the video cannot be downloaded or converted
        st.error("Download failed!")
else :
    if st.button("Convert to MP3"):
        try:
            with st.spinner("Converting..."):
                video = VideoFileClip(mp4_url)
                audio = video.audio
                audio.write_audiofile("output.mp3")
            st.success("Conversion successful!")
        except:
            st.error("Conversion failed.")
        with open("output.mp3", "rb") as f:
            byte_content = f.read()
            st.download_button(
                label="Download MP3",
                data=byte_content,
                file_name="output.mp3",
                mime="audio/mpeg",
            )


