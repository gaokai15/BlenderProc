import math
import os
import itertools
import random
import sys


my_path = os.path.abspath(os.path.dirname(__file__))


def add_object(ID, name, path, config_file_path):
    '''
    ID: int YCB index, e.g. 37
    name: string e.g. 037_scissors
    path: string obj file dir
    config_file_path: config file dir
    '''
    f = open(config_file_path, 'a')
    f.write("    # Load obj "+str(ID)+"\n")
    f.write("    {\n")
    f.write("      \"module\": \"loader.ObjectLoader\",\n")
    f.write("      \"config\": {\n")
    f.write("        \"path\": \""+path+"\",\n")
    f.write("        \"add_properties\": {\n")
    f.write("          \"cp_physics\": True,\n")
    f.write("          \"cp_category_id\": \""+ str(ID) +"\",\n")
    f.write("          \"cp_name\": \""+name+"\"\n")
    f.write("        }, \n")
    f.write("        \"cf_set_shading\": \"SMOOTH\"\n")
    f.write("      },\n")
    f.write("    },\n")
    f.close()


def write_config(num_obj=10):
    object_list = [
        "005_tomato_soup_can",
        "007_tuna_fish_can",
        "008_pudding_box",
        "009_gelatin_box",
        "010_potted_meat_can",
        "011_banana",
        "013_apple",
        "014_lemon",
        "016_pear",
        "017_orange",
        "025_mug",
        "037_scissors",
        "040_large_marker",
        # "049_small_clamp",
        "055_baseball",        
        "061_foam_brick"
    ]
    template_f = open(os.path.join(my_path, "empty_config.yaml"), 'r')
    empty_world_lines = list(template_f.readlines())
    f = open(os.path.join(my_path, "config.yaml"), 'w')
    f.writelines(empty_world_lines[:32])
    f.close()
    option_list = list(itertools.combinations(object_list, num_obj))
    random.shuffle(option_list)
    selected_objects = option_list[0]
    for obj_name in selected_objects:
        ID = int(float(obj_name[:3]))
        obj_path = os.path.join(my_path, "ycb", obj_name, "google_16k", "textured.obj")
        config_file_path = os.path.join(my_path, "config.yaml")
        add_object(ID, obj_name, obj_path, config_file_path)
    f = open(os.path.join(my_path, "config.yaml"), 'a')
    f.writelines(empty_world_lines[32:])
    f.close()
    template_f.close()


def single_scene(sceneID, num_obj):
    print( "renewing config")
    write_config(num_obj)
    run_file_path = os.path.dirname(os.path.dirname(my_path))
    os.system("python "+os.path.join(run_file_path,"run.py") + " " +\
        os.path.join(my_path, "config.yaml") +" "+\
        os.path.join(my_path, "output") + " " +\
        os.path.join(my_path, "camera_positions") + " "+\
        os.path.join(run_file_path, "resources", "cctextures") +"\n")



def main():
    num_obj_options = []
    for num in range(2,11):
        num_obj_options += [num]*num
    for sceneID in range(2):
        num_obj = random.choice(num_obj_options)
        print( "##############################")
        print( "sceneID", sceneID, "num_obj", num_obj)
        print( "##############################")
        single_scene(sceneID, num_obj)



if __name__ == "__main__":
    main()
