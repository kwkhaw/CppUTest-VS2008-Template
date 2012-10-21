import fileinput
import shutil
import subprocess
import os

project_name = raw_input("Enter your project name: ")

# Generate GUID
p = subprocess.Popen(["C:\\Program Files\\Microsoft Visual Studio 9.0\\Common7\\Tools\\uuidgen", "-c"], stdout=subprocess.PIPE)
uuid, err = p.communicate()

uuid = uuid.strip()

templates_dir = './Templates/'
new_proj_dir = './' + project_name + '/'

# Create a directory for the project
if not os.path.exists(new_proj_dir):
    os.makedirs(new_proj_dir)
    
# Create a copy of the vcproj file
template_vcproj_file = templates_dir + 'Template.vcproj'
new_vcproj_file = new_proj_dir + project_name + '.vcproj'
shutil.copyfile(template_vcproj_file, new_vcproj_file)

# Create a copy of the .cpp file
template_cpp_file = templates_dir + 'Template.cpp'
new_cpp_file = new_proj_dir + project_name + '.cpp'
shutil.copyfile(template_cpp_file, new_cpp_file)

# Create a copy of the SampleUnitTest.cpp file
sample_unit_test_cpp_file = 'SampleUnitTest.cpp'
src = templates_dir + sample_unit_test_cpp_file
dst = new_proj_dir + sample_unit_test_cpp_file
shutil.copyfile(src, dst)

# Replace GUID and project name
for line in fileinput.FileInput(new_vcproj_file,inplace=1):
    line = line.replace("Template", project_name)
    print line,

for line in fileinput.FileInput(new_vcproj_file,inplace=1):
    line = line.replace("uuid", uuid)
    print line,

raw_input('Press Enter to exit')