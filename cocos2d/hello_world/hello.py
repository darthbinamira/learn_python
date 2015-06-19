from cocos import *

class HelloWorld(layer.Layer):
    
    def __init__(self):
        super(HelloWorld, self).__init__()
        label = text.Label('Hello, World!',
                            font_name = 'Times New Roman',
                            font_size = 32,
                            anchor_x = 'center',
                            anchor_y = 'center')
        label.position = 320, 240
        self.add(label)

director.director.init()

hello_layer = HelloWorld()

main_scene = scene.Scene(hello_layer)

director.director.run(main_scene)

