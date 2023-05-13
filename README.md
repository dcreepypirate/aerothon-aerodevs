
# AeroGreen

**A platform that enables seamless communication and collaboration among aircraft manufacturers, airlines, and recycling facilities, fostering a cooperative ecosystem for sustainable component management.**

## Prerequisites

- Python 3.x
- `pip` package manager

## Setup Instructions

1. **Create a virtual environment:**

   ```bash
   python -m venv env
2. **Activate the virtual environment:**
   ```bash
   source env/bin/activate
3. **Install the project dependencies:**
	 ```bash
	pip install -r requirements.txt
4. **Apply database migrations:**
	 ```bash
	 python manage.py makemigrations
	python manage.py migrate
5. **Start the development server:**
	```bash
	python manage.py runserver
6. **Start the development server:**
	Open a web browser and visit [http://localhost:8000](http://localhost:8000/) to view the application.

## Project Objective:
Create an aircraft sustainability platform connecting manufacturers, airlines, and recycling facilities for collaborative end-of-life component repurposing and recycling. Improve resource utilization, environmental sustainability, compliance, and economic opportunities in aviation. Revolutionize component management.

## Solution:
AeroGreen is an innovative solution aimed at revolutionizing the repurposing and recycling of end-of-life aircraft components. The project involves the development of a comprehensive platform that connects aircraft manufacturers, airlines, and recycling facilities. By creating a seamless ecosystem for collaboration and resource optimization, the platform aims to promote environmental sustainability, ensure regulatory compliance, and generate economic opportunities within the aviation industry.

Through the platform, stakeholders can efficiently manage the repurposing and recycling of end-of-life aircraft components. The system enables streamlined communication and collaboration, allowing manufacturers to identify and label components, airlines to track and manage their inventory, and recycling facilities to efficiently process and repurpose the components.

## Methodology:
1. Requirement Gathering: Understanding the needs by studying the given data on aircraft parts and researching for similar deployed websites for reference.
2. Design and Architecture: Based on the gathered requirements, a detailed design and architecture plan is created. This includes defining the system components, data models, user interfaces, and integration points with external systems. 
3. Agile Development: The development of the platform follows an Agile methodology, which involves breaking down the project into smaller tasks or user stories. This iterative approach allows for continuous feedback, adaptation, and early identification of any issues or changes required.
4. Technology Selection: Django framework allows for integration of front end tools(HTML, CSS, JavaScript, Bootstrap) and backend tools(SQLite)
5. Testing and Quality Assurance: Unit testing of each individual components( such as Navigation bar, search option, product grid) is done. Integration test allows for recognition of errors within modules at earlier stage.
6. Deployment and Integration: The platform is deployed on a local environment. It is integrated with external systems, such as aircraft parts' databases, and user database, to enable seamless data exchange and synchronization.
7. Continuous Improvement: The development and deployment of the platform are not the end of the process. Continuous improvement is key to refining the platform based on user feedback, market demands, and emerging technologies. Regular updates, enhancements, and feature additions are planned and implemented to ensure the platform remains up-to-date and aligned with the evolving needs of the stakeholders.

## Key Features:
~A database of aircraft parts with information on their material composition, age, and condition, among other things.
~Manufacturers and airlines should purchase/identify components reaching the end of their useful life and arrange for their repurposing or recycling.
~Recycling facilities identify recycled material sources, which include both metals and nonmetallic materials such as composites and plastics.
~A visual overview of recycled and repurposed materials
~Environmental impact measures to demonstrate the beneficial effects of recycling and reusing Performance metrics to monitor the performance of circular economy models
