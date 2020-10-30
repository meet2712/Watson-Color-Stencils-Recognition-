import streamlit as st
import json,os
from PIL import Image
import warnings
warnings.filterwarnings("ignore")


st.header("Color Recognition")

import json
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='V6sqBLd8I4ixf3_4cUSMTi7Smm1XmNeTkn7Hwr9Zr526')

images_file = st.file_uploader("Upload Image Here ",type=["jpg","png","jpeg"])

# image_preview = Image.open(image_file)
# st.image(image_file,caption="uploaded image",use_column_width=True)




if images_file is not None:
    if st.button("classify image"):
        classes = visual_recognition.classify(
            images_file,classifier_ids='DefaultCustomModel_632239058').get_result()



        # st.subheader("Json Response")
        # st.json(json.dumps(classes, indent=2))
        # print(json.dumps(classes, indent=2))

        st.subheader("Output:")
        st.write("Class: ",classes["images"][0]["classifiers"][0]["classes"][0]["class"])
        st.write("Score: ",classes["images"][0]["classifiers"][0]["classes"][0]["score"])



        # image = Image.open(images_file)
        # st.image(image, caption='Uploaded Image.', use_column_width=True)






#
# with open('/content/25.jpg', 'rb') as images_file:
#     classes = visual_recognition.classify(
#         images_file,
#         threshold='0.6',
#         classifier_ids='DefaultCustomModel_632239058').get_result()
# print(json.dumps(classes, indent=2))