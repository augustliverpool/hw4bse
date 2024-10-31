from setuptools import setup, find_packages

# 先读取README.md文件的内容
with open('README.md', 'r') as file:
    long_description = file.read()

setup(
    name='my_diabetes_library', 
    version='0.1.0',  
    author='weisun',  
    author_email='1048199440sun@gmail.com', 
    description='A library for diabetes data analysis and prediction',
    long_description=long_description,  
    long_description_content_type='text/markdown',  
    url='https://github.com/yourusername/my_diabetes_library',   
    packages=find_packages(),  
    classifiers=[
        'Programming Language :: Python :: 3',  
        'License :: OSI Approved :: MIT License',  
        'Operating System :: OS Independent',  
    ],
    python_requires='>=3.6',  
    install_requires=[  
        'pandas',  
        'scikit-learn',  
    ],
)
