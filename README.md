<p style="text-align: center; font-size: 30px; font-weight : bold;">2022 Purdue Project<p>

![](https://i.imgur.com/KMHj3Al.jpg)

📑 _Project Title_

    Cost-Effective Fallen Tree Recognition Solution utilizing YOLOX Object Detecting Algorithm and Visualization.

📅 _Project Period_

    01-01-2022(SUN) ~ 02-26-2022(MON)

🧖🏻‍♀️ _Problem Statement_

    The effects of strong winds from tropical cyclones on the forest ecosystem have been reported in many studies, especially disturbing the forest ecosystem.
    If information on the location and distribution of fallen trees can be quickly identified and measures such as tree removal or preservation can be secured,
    additional damage such as damage to the forest ecosystem and financial loss of forest owners can be minimized.

💡 _Novelty_

    1. Suggest a cost-effective way!
       Our research aims to suggest a cost-effective way that small-scale farm owner and low budget research can utilize to get their desired result.
       Most research use high-performance equipments ensures high accuracy in geographical observation.
       However, those equipments require high expenses to operate, which could be a financial strain to our stakeholder.
       So it is not suitable to our research since we do focus on suggesting a cost-effective solution to our stakeholder.
       To overcome this problem, we’ve decided to use camera-equipped UAV so that our stakeholder can easily access the result.

    2. Solution to be easily utilized using visualization!
       An efficient approach is needed to quickly grasp information on the location and distribution of fallen trees.
       Therefore, by visualizing the information on fallen trees identified through UAV in a use-friendly manner,
       the user can more accurately determine the extent of the damage.
       This can be used for agricultural insurance, government compensation claim support, forest management, and ecological monitoring.

🏛 _System Overview_

<p align="center">
   <img src="https://i.imgur.com/E2PAVi8.png" width="600" alt="Image Error"/>
</p>
    
    1. Enter the picture taken by uav into the client
    
    2. Client sends the picture to the server
    
    3. The server analyzes the image using the trained model
    
    4. Returns the analyzed results to the client.
    
    5. Client visualizes the results.

<p align="center">
   <img src="https://i.imgur.com/Red1Sdd.png" width="600" alt="Image Error"/>
</p>

    🌳 Model(PC1): The YOLOX-x model, which guarantees high accuracy among the YOLOX series to which the anchor-free manner is applied, was used.
    Train data is the VOC dataset format of the image obtained by dividing the image collected through UAV into 10 frames.
    It is a multi-class classification because it is classified into three classes: normal, broken, and down.
    The model was trained to have high accuracy by adjusting hyperparameters using the GPU of the Colab.
    When the model was evaluated through mAP, a performance evaluation, it showed between 75% and 80% accuracy.

    🌳 Backend(PC1): In the backend, the Django-Rest framework was used. REST API was used for transfering data to frontend.
    When the data is received from client, it is passed to the trained model to detect fallen tree. The result consisting of amount of fallen tree was stored to DB, MySQL.
    And the data consisting image or video was stored to S3(AWS).
    For server, EC2(AWS) was used

    🌳 Frontend(PC2): Using React with JavaScript, provide visualization.
    Rest api was used for communication with the server.
    For environment setting, webpack, babel, prettier, eslint are used.
    For test, jest, storybook, react-testing-library are used.

🖥️ _Environment Setting_

    ✔️Python version 3.8.8

    ✔️Django version 4.0.2

📤 _Installation_

    - Frontend
    $ git clone https://github.com/Bikini-city/Tree-Visualization
    $ cd Tree-Visualization
    $ touch .env
    $ npm install
    $ npm run dev

    - Backend
    $ git clone https://github.com/Bikini-city/Visualization_backend.git
    $ pip install requirements.txt
    (++fallentree/setting.py에서 secret_key와 db설정)
    $ cd fallentree
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py runserver 0.0.0.0:8000

👨‍👩‍👧‍👧 _Collaborator_

    👨🏻‍💻Eunsik Park
       -Chungnam National Univeristy
       -Major in Computer Science Engineering
       -qkrdmstlr3@cnu.ac.kr
       -https://github.com/qkrdmstlr3

    👩🏻‍💻Junghyun Moon
       -Chungnam National University
       -Major in Computer Science and Engineering
       -mjh991016@cnu.ac.kr
       -https://github.com/MoonDD99

    👩🏻‍💻Hearim Moon
       -Chungnam National University
       -Major in Computer Science and Engineering
       -ansgpfla7@cnu.ac.kr
       -https://github.com/moo-nerim

    👩🏻‍💻Juyeong Lee
       -Chungnam National Univeristy
       -Major in Computer Science and Engineering
       -lge2515@cnu.ac.kr
       -https://github.com/2Ju0

    👨🏻‍💻Doyoon Kim
       -Purdue University
       -Major in Computer and Information Technology
       -kim3312@purdue.edu
       -https://github.com/doyoonkim3312
