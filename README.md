# MP4 to MP3 Converter

This is a simple MP4 to MP3 converter that works for both YouTube and non-YouTube video links. It is built using Python and the following libraries:

- `streamlit`: for creating the user interface.
- `moviepy`: for converting audio from video files to MP3 format.
- `pytube`: for downloading YouTube videos.

## How to use

To use the converter, follow these steps:

1. Enter the URL of the MP4 video you want to convert in the text input field.
2. If the URL is a YouTube link, the video details such as title, duration and views will be displayed to the user.
3. Click on the "Convert to MP3" button to start the conversion process.
4. If the conversion is successful, a success message will be displayed along with a download button for the converted MP3 file.
5. Click on the download button to download the MP3 file.

## Running the converter

To run the converter on your machine, follow these steps:

1. Install the required libraries by running `pip install -r requirements.txt` in your terminal.
2. Clone the repository using `git clone https://github.com/your-username/mp4-to-mp3-converter.git`.
3. Navigate to the project directory using `cd mp4-to-mp3-converter`.
4. Run the converter using `streamlit run app.py`.
5. The converter will open in your default web browser.

## Demo

You can see a live demo of the MP4 to MP3 converter [here](https://deepankarvarma-mp4-to-mp3-converter-using-python-app-pyuc6s.streamlit.app/).
