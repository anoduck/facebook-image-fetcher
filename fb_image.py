## Library for url retrieval
try:
    import urllib
    import sys
    import os
    import datetime
    import json
except:
    raise "Dependencies not found."

## Helper functions start
def create_dir(prefix):
    dir_c = os.path.join(os.getcwd(), prefix, datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
    try:
        os.makedirs(dir_c)
    except OSError, e:
        if e.errno != 17:
            pass
        else:
            print "Cannot create folder. Try again."
            exit
    return dir_c

def gen_url(name):
    return "http://graph.facebook.com/picture?id=" + name + "&width=800"

def get_profile(photo_url, save_url):
    print "Fetching " + photo_url + " ..."
    urllib.urlretrieve(photo_url, save_url)
    return [photo_url, save_url]

def get_profile_of_id(id1, id2):
    photo_data = {}
    photo_count = 1
    folder = create_dir('fb-image')
    for i in xrange(int(id1), int(id2) + 1):
        photo_data[photo_count] = get_profile(gen_url(str(i)), folder + "/" + str(i) + ".jpg")
        photo_count += 1
    json.dump(photo_data, open(folder + "/data.txt", 'wb'))
    print "Images fetched: " + str(photo_count - 1)
    return 0    
    
def get_profile_of_file(filename):
    names = []
    with open(filename) as f:
        content = f.readlines()
    for i in content:
        names.append(i.rstrip('\n').lstrip(' '))
    photo_data = {}
    photo_count = 1
    folder = create_dir('fb-image')
    for i in names:
        photo_data[photo_count] = get_profile(gen_url(i), folder + "/" + str(i) + ".jpg")
        photo_count += 1
    json.dump(photo_data, open(folder + "/data.txt", 'wb'))
    print "Images fetched: " + str(photo_count - 1)
    return 0
## Helper functions end

def main():
    in_name = list(sys.argv[1:])
    if len(in_name) == 1: get_profile_of_file(in_name[0])
    elif len(in_name) == 2: get_profile_of_id(in_name[0], in_name[1])
    else: print "Wrong input. Please try again."
    return 0
        

if __name__ == "__main__":
    main()
