from django.shortcuts import render

# Create your views here.

def index(request): 
    skill= [
            {"skill_name": "Data visualization", "skill_level": "intermediate"},
            {"skill_name": "data cleaning", "skill_level": "intermediate"},
            {"skill_name": "django", "skill_level": "intermediate"},
            {"skill_name": "FastApi", "skill_level": "intermediate"},
            {"skill_name": "Machine Learning", "skill_level": "intermediate"},
        ]  
    data_context = {
        "page_title": "Portfolio-Narayan",
        "name": "Narayan Prasad Ghimire",
        "role": "Data Scientist",
        "about1": "I am a passionate and detail-oriented Data Scientist dedicated to turning raw data into meaningful insights and impactful solutions. With a strong foundation in Python, statistics, and machine learning, I enjoy solving real-world problems through data-driven approaches.",
        "about2": "My journey in data science is driven by curiosity and continuous learning. I have worked on projects involving data cleaning, exploratory data analysis (EDA), predictive modeling, and building machine learning systems. From student grade prediction using multi-linear regression to developing recommendation systems and data processing pipelines, I focus on creating practical, scalable, and production-ready solutions.",
        
        "skills":skill,

        "project":[
            # {"project_name":"Password checker","project_image": "image/pw_checker.jpg", "project_description": "", "link":""},
            {"project_name":"User management api ","project_image":"image/user_mgmt.png", "project_description": "", "link":"https://github.com/Narayan210/User-management-api.git"},
            {"project_name":"student management system api","project_image":"image/school mgmt.jpg", "project_description": "","link":"https://github.com/Narayan210/std_mgmt_system_api.git"},
            {"project_name":"Movie Recomendation system","project_image":"image/movie_recomendation.jpg", "project_description": "", "link":"https://github.com/Narayan210/Movie-Recomendation-system-using-ml.git"},
        ]
    }
    return render(request, "portfolio/index.html", data_context)

def resume_view(request):
    return render(request, 'portfolio/resume.html')