import time
t1 = time.time()
lst = [
    'python is good',
    'is python good?',
    'python is python',
    'this is a python string',
    'python is easy',
    'python is fun',
    'hello python',
    'python is powerful',
    'python is versatile',
    'python is popular',
    'python is amazing',
    'python is fantastic',
    'python is the best',
    'python is awesome',
    'learn python',
    'python is everywhere',
    'python is love',
    'python is life',
    'do you like python?',
    'python is my favorite language',
    'python is great for beginners',
    'python is widely used',
    'python is for everyone',
    'what can you do with python?',
    'python is open source',
    'python is highly readable',
    'python is dynamically typed',
    'python is statically typed',
    'python is interpreted',
    'python is compiled',
    'python is object-oriented',
    'python is procedural',
    'python is functional',
    'python is used in web development',
    'python is used in data science',
    'python is used in artificial intelligence',
    'python is used in machine learning',
    'python is used in automation',
    'python is used in robotics',
    'python is used in game development',
    'python is used in scientific computing',
    'python is used in desktop applications',
    'python is used in mobile applications',
    'python is used in embedded systems',
    'python is used in network programming',
    'python is used in cybersecurity',
    'python is used in finance',
    'python is used in education',
    'python is used in research',
    'python is used in government',
    'python is used in healthcare',
    'python is used in entertainment',
    'python is used in space exploration',
    'python is used in aviation',
    'python is used in automotive industry',
    'python is used in agriculture',
    'python is used in environmental science',
    'python is used in telecommunications',
    'python is used in social media',
    'python is used in e-commerce',
    'python is used in digital marketing',
    'python is used in content management systems',
    'python is used in blogging platforms',
    'python is used in forums',
    'python is used in wikis',
    'python is used in online learning platforms',
    'python is used in project management tools',
    'python is used in version control systems',
    'python is used in collaboration tools',
    'python is used in communication tools',
    'python is used in testing frameworks',
    'python is used in deployment tools',
    'python is used in continuous integration systems',
    'python is used in monitoring systems',
    'python is used in logging systems',
    'python is used in error tracking systems',
    'python is used in security tools',
    'python is used in performance optimization',
    'python is used in data visualization',
    'python is used in reporting',
    'python is used in analytics',
    'python is used in business intelligence',
    'python is used in decision support systems',
    'python is used in natural language processing',
    'python is used in computer vision',
    'python is used in speech recognition',
    'python is used in sentiment analysis',
    'python is used in recommendation systems',
    'python is used in chatbots',
    'python is used in virtual assistants',
    'python is used in autonomous vehicles',
    'python is used in drones',
    'python is used in wearable technology',
    'python is used in internet of things',
    'python is used in smart homes',
    'python is used in smart cities',
    'python is used in smart grids',
    'python is used in renewable energy',
    'python is used in climate modeling',
    'python is used in disaster management',
    'python is used in emergency response systems',
    'python is used in public safety',
    'python is used in transportation',
    'python is used in logistics',
    'python is used in supply chain management',
    'python is used in inventory management',
    'python is used in retail',
    'python is used in sales forecasting',
    'python is used in customer relationship management',
    'python is used in human resources',
    'python is used in accounting',
    'python is used in billing systems',
    'python is used in payroll processing',
    'python is used in tax preparation',
    'python is used in financial analysis',
    'python is used in risk management',
    'python is used in compliance',
    'python is used in legal services',
    'python is used in intellectual property management',
    'python is used in contract management',
    'python is used in document management',
    'python is used in records management',
    'python is used in archives',
    'python is used in libraries',
    'python is used in museums',
    'python is used in galleries',
    'python is used in theaters',
    'python is used in cinemas',
    'python is used in concerts',
    'python is used in festivals',
    'python is used in exhibitions',
    'python is used in conferences',
    'python is used in conventions',
    'python is used in trade shows',
    'python is used in workshops',
    'python is used in seminars',
    'python is used in symposiums',
    'python is used in summits',
    'python is used in hackathons',
    'python is used in meetups',
    'python is used in networking events',
    'python is used in training sessions',
    'python is used in team-building activities',
    'python is used in corporate retreats',
    'python is used in incentive trips',
    'python is used in offsite meetings',
    'python is used in virtual events',
    'python is used in hybrid events',
    'python is used in gamification',
    'python is used in augmented reality',
    'python is used in virtual reality',
    'python is used in mixed reality',
    'python is used in immersive experiences',
    'python is used in 3D modeling',
    'python is used in simulations',
    'python is used in visualization',
    'python is used in prototyping',
    'python is used in product design',
    'python is used in user experience',
    'python is used in user interface',
    'python is used in interaction design',
    'python is used in information architecture',
    'python is used in graphic design',
    'python is used in typography',
    'python is used in illustration',
    'python is used in photography',
    'python is used in video production',
    'python is used in animation',
    'python is used in motion graphics',
    'python is used in audio production',
    'python is used in sound design',
    'python is used in music composition',
    'python is used in game design',
    'python is used in level design',
    'python is used in character design',
    'python is used in asset creation',
    'python is used in environment design',
    'python is used in lighting design',
    'python is used in texture mapping',
    'python is used in rigging',
]
pattern = 'design'

count = []
match = []

for i in lst:
    if i.find(pattern) >= 0:
        count.append(i.count(pattern))
        match.append(i)

for i in range(0,len(count)-1):
    if count[i] < count[i+1]:
        count[i],count[i+1] = count[i+1],count[i]
        match[i],match[i+1] = match[i+1],match[i]

for i in match:
    print(i)
t2 = time.time()
print(f"search in {t2-t1} seconds")