from fasthtml.common import *

users = [
    {
      'name': "Sophia Gonzalez",
      'position' : 'Software Engineer',
      'img': "https://i.pravatar.cc/150?img=1",
      'details' : 'Skilled in designing and implementing robust software solutions for large-scale systems. Proficient in languages such as C++, Java, and Python. Strong understanding of data structures, algorithms, and system architecture to create efficient, scalable, and maintainable code',
      'id': '1',
    },
    {
      'name': "Ben Allen",
      'position' : 'Mobile Application Developer:',
      'img': "https://i.pravatar.cc/150?img=5",
      'details' : 'Specializes in developing mobile applications for iOS and Android platforms using Swift, Kotlin, or cross-platform tools like Flutter. Experience in integrating RESTful APIs and maintaining high-quality code with a focus on performance and user experience.',
      'id': '2',
    },
    {
      'name': "Jill Fernandez",
      'position' : 'DevOps Engineer',
      'img': "https://i.pravatar.cc/150?img=51",
      'details' : 'Specializes in CI/CD pipeline creation and cloud infrastructure management using Docker, Kubernetes, and Jenkins. Strong background in scripting and automation with Python and Bash, as well as experience with version control systems like Git.',
      'id': '3',
    },
    {
      'name': "Cynthia Obel",
      'position' : 'Back-End Developer',
	  'img': "https://i.pravatar.cc/150?img=34",
      'details' : 'Skilled in server-side programming with expertise in Node.js, Python, and Java. Proficient in working with databases (SQL and NoSQL) and developing RESTful APIs. Strong understanding of server architecture and cloud services like AWS',
	  'id': '4',
    },
  ]

hdrs = (
    Link(rel="stylesheet", href="public/app.css", type="text/css"),
    #Script(src='https://cdn.tailwindcss.com'),
    Style(''' 
        .fade-in {
            animation: fadeIn 1.5s ease-out;
        }

        @keyframes fadeIn {
        from {            
            opacity: 0;
        }
        to {         
            opacity: 1;
        }
        }
    '''),
)

app, rt = fast_app(live=True, pico=False, hdrs=hdrs)

@rt("/{fname:path}.{ext:static}")
def get(fname:str, ext:str): 
    return FileResponse(f'public/{fname}.{ext}')



def item(user):
    return Li(
        Img(src=user['img'], alt='User Avatar', cls='w-12 h-12 rounded-full mr-4', style=f"view-transition-name: img-{user['id']}"),
        Div(
            H2(user['name'], cls='text-lg font-semibold', style=f"view-transition-name: name-{user['id']}"),
            P(user['position'], cls='text-sm text-gray-600'), style=f"view-transition-name: position-{user['id']}",
            cls='flex-1'
        ),
        hx_get=f"/get_user/{user['id']}",
        hx_target="#list",
        hx_swap='innerHTML transition:true',
          
      
        
        cls='flex items-center bg-white shadow-md p-4 rounded-lg cursor-pointer'
    )

def card(user):
    return Div(
    Img(src=user['img'], alt='User Avatar', cls='w-48 h-48 rounded-full object-cover', style=f"view-transition-name: img-{user['id']}"), 
    Div(
        H3(user['name'], cls='text-xl font-semibold mb-2',  style=f"view-transition-name: name-{user['id']}"),
        P(user['position'], cls='text-sm text-gray-500 mb-4', style=f"view-transition-name: position-{user['id']}"),
        P(user['details'], cls='text-gray-700 transition duration-300 ease-in opacity-100 fade-in'),
        cls='p-4'
    ),
    Button('Back',
        hx_get='/', hx_target="#list", hx_swap="innerHTML transition:true",
        cls='flex items-center px-4 py-2 bg-gray-200 text-gray-700 rounded hover:bg-gray-300 transition duration-300 ease-in-out'
        ),
    cls='flex flex-col items-center'
)


def list_of_users(users):
    return Ul(*[item(user) for user in users],id="list", cls='space-y-4')       
   

@rt('/')
def main():
        return Div(
            list_of_users(users),
            cls="flex items-center justify-center max-w-sm min-h-screen mx-auto"
        )

@rt('/get_user/{id}')
def get(id:str):
    user = next((user for user in users if user['id'] == id), None)
    return card(user)


serve()
