from ml_models.detect_image import DetectImage


class MLModelService:

    @staticmethod
    def find_plant_name(image_file):
        image_path = ""
        # save image here
        # result = detect(image_file)
        #  process result
        # delete the saved image
        # DetectImage detectImage = new  DetectImage()
        #print("Searching plant name")
        result = DetectImage.detect(image_file)
        return result

# if __name__ == '__main__':

#     class_names = MLModelService.find_plant_name('backend/tulsi.png')
#     print("Detected classes:", class_names)
