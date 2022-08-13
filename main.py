from flask import Flask
from flask_restx import Resource, Api
from werkzeug.datastructures import FileStorage  

from backend import preprocessing
import random 
import os


app = Flask(__name__)
api = Api(app, version='1.0',
          title='Surface crack detection ',
          description='cnn and vgg16')

api.namespace('Note 
                   description="Whatever your namespace is Please upload the wall's visual image.")
upload_parser = api.parser()
upload_parser.add_argument('file', location='files',
                           type=FileStorage, required=True)






@api.route('/model_Cnn/')
@api.expect(upload_parser)
class Model_Cnn(Resource):
    def post(self):
        
        args = upload_parser.parse_args()
        uploaded_file = args['file']  # This is FileStorage instance
        print(uploaded_file)
        url = uploaded_file
        #result = image_transform.model_predict(url)
        print(url)
        print("url:::::",url)
        filename = str(random.randint(1,10000))+'.jpg'
        filepath = os.path.join("uploads",filename)
        url.save(filepath)
        print("File saved")
        if os.path.exists(filepath):
            result = preprocessing.predict_image(filepath)
            print(result)
            if result == 1:
                print(result,"OOPS!!! There is a crack")#positive1
                return "POSITIVE,Crack detected",201
            else:
                print(result,"There is no crack")#negative0
                return "NEGATIVE,No crack",201

        
        # def load(url,model):
        #     """
        #     ***Function used to predict cracks are present in the wall or not***
        #     params:
        #     filename :Path of the image where it is located
        #     model:trained cnn model which help us to predict 
        #     returns:result retrns the output
        #     """
        #     np_image = Image.open(url)
        #     np_image = np.array(np_image).astype('float32')/255
        #     np_image = transform.resize(np_image, (120, 120, 3))
        #     np_image = np.expand_dims(np_image, axis=0)
        #     k.clear_session()
        #     predictions = model.predict(np_image)
        #     result = np.round(predictions)
            
            # return result
        #result =load(url,modelVGG) 
        return result, 201
if __name__ == '__main__':
    app.run(debug=True)
