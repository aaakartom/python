import os
import json


def write_json_file():
    with open("exercise23_beyond3__support_file.json", 'w') as json_file:
        user_input = input('Enter the directory:')
        list_of_files = os.listdir(f'C://Users/Artyom/{user_input}')

        dict_of_file_info = {}
        for file in list_of_files:
            file_stats = os.stat(f'C://Users/Artyom/{user_input}/{file}')
            size = file_stats.st_size
            modification_time = file_stats.st_mtime
            file_info = {"md_time":  modification_time, "size": size}
            dict_of_file_info[file] = file_info

        json_object = json.dumps(dict_of_file_info)
        json_file.write(json_object)


def info_analyzing():
    with open("exercise23_beyond3__support_file.json", 'r') as json_file:
        file_contents = json.load(json_file)

        most_recent = 0
        largest = 0

        for file in file_contents:
            dict_of_info = file_contents[file]
            if most_recent < dict_of_info['md_time']:
                most_recent = dict_of_info['md_time']
                most_recent_file = file
            if largest < dict_of_info['size']:
                largest = dict_of_info['size']
                largest_file = file
        print(f"Most recent: {most_recent_file}")
        print(f"Largest: {largest_file}")

        least_recent = most_recent
        smallest = largest

        for file in file_contents:
            dict_of_info = file_contents[file]
            if least_recent > dict_of_info['md_time']:
                least_recent = dict_of_info['md_time']
                least_recent_file = file
            if smallest > dict_of_info['size']:
                smallest = dict_of_info['size']
                smallest_file = file
        print(f"Least recent: {least_recent_file}")
        print(f"Smallest: {smallest_file}")


write_json_file()
info_analyzing()