from backend.models import model_config
#from models import model_config
import os
import numpy as np
from skimage import transform
from PIL import Image 
model_path = model_config.model_path
model = model_config.model_loading()
# user_input = r'D:\Surface Crack Detection\data\Positive\00002.jpg'
# open_image = Image.open(user_input) 
# convert_img_to_array = np.array(open_image).astype('float32')/255
# transforming_image =transform.resize(convert_img_to_array, (120, 120, 3))
# np_image = np.expand_dims(transforming_image, axis=0)          
# predictions = model.predict(np_image)
# result = np.round(predictions)
# print(result)


def predict_image(user_input):
    
    try:
        if os.path.exists(user_input):
            print('image Loaded')
        open_image = Image.open(user_input) 
        convert_img_to_array = np.array(open_image).astype('float32')/255
        transforming_image =transform.resize(convert_img_to_array, (120, 120, 3))
        np_image = np.expand_dims(transforming_image, axis=0)          
        predictions = model.predict(np_image)
        result = np.round(predictions) 
        return result
    
    
    except Exception as e:
        return str(e)
    
    
    finally:
        print("Model Predicted")
    
        
        # if result  == 1:
        #     return "positive"
        
        # else :
        #     return "negative"
    
   
url = (r"D:\SurfaceCrackDetection\data\Negative\00030.jpg")
print(predict_image(url))
           
            





           
# user_input = r'D:\Surface Crack Detection\data\Positive\00002.jpg'
# def predict_result(model_loading,user_input):
#     try:
#         if os.path.exists(user_input):
#             print("path is valid") 
         
#         if model is None:
#             model = model_loading() 
#             print(model)
                   
#             # open_image = Image.open(user_input) 
#             # convert_img_to_array = np.array(open_image).astype('float32')/255
#             # transforming_image =transform.resize(convert_img_to_array, (120, 120, 3))
#             # np_image = np.expand_dims(transforming_image, axis=0)          
#             # predictions = model.predict(np_image)
#             # return predictions
#     except Exception as e:
#         print(str(e))
     
           
# print(predict_result(model_loading,user_input))
