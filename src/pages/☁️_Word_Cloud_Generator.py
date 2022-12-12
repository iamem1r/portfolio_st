import time
from io import StringIO

import arabic_reshaper
import streamlit as st
from bidi.algorithm import get_display
from hazm import Normalizer, word_tokenize
from loguru import logger
from wordcloud import WordCloud
from data import DATA_DIR

st.set_page_config(page_title="Word Cloud Generator", page_icon='☁️')

st.title("Word Cloud Generator")

st.write("""
- This is a simple **WordCloud** generator application.
- Drop your text file and then 💣**BOOOOM**💣 !
- It will read the file, **normalize** and **removing stop words** and generates a word cloud.
""")

st.write("****")

if "upload_file" in st.session_state:
    st.session_state["upload_file"] = "not_uploaded"


def change_upload_file_state():
    st.session_state["upload_file"] = "uploaded"


normalizer = Normalizer()


st.subheader("Upload your file")

text_file = st.file_uploader(
    label="",
    type='.txt',
    key='text_file',
    help='.txt file up to 200MB',
    label_visibility='collapsed',
    on_change=change_upload_file_state
)


stopwords = open(DATA_DIR / 'assets' / 'stopwords.txt').readlines()
stopwords = list(map(str.strip, stopwords))
stopwords = list(map(normalizer.normalize, stopwords))


if st.session_state['upload_file']:
    # To convert to a string based IO:
    if text_file is not None:
        stringio = StringIO(text_file.getvalue().decode("utf-8"))
        # To read file as string:
        text = stringio.read()
        tokens = word_tokenize(text)
        tokens = list(filter(lambda x: x not in stopwords, tokens))
        new_text = ''
        new_text += f" {' '.join(tokens)}"

        # reshape, and normalize text content
        logger.info("Reshape and normalizing text")
        new_text = normalizer.normalize(new_text)
        new_text = arabic_reshaper.reshape(new_text[:500000])
        new_text = get_display(new_text)

        # generate wordcloud
        logger.info("Generating wordcloud...")
        wordcloud = WordCloud(
            font_path=str('assets/Mitra_Bold.ttf'),
            width=1800,
            height=1200,
            background_color='white'
        ).generate(new_text)

        progress_bar = st.progress(0)
        for per_progress in range(100):
            time.sleep(0.01)
            progress_bar.progress(per_progress+1)

        st.write("\n")
        st.write("\n")

        st.subheader("Here is your wordcloud 👇🏻")

        st.write("\n")

        image = wordcloud.to_image()
        st.image(image)

        # with open(os.getcwd(), "rb") as file:
        #     btn = st.download_button(
        #         label="Download image",
        #         data=image,
        #         file_name="wordcloud.png",
        #         mime="image/png"
        #     )

    else:
        pass
