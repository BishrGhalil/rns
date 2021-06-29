# Print List func
def printlist(org, enum = False):
    if enum:
        for index, item in enumerate(org):
            print(index + 1, item)
    else:
        for item in org:
            print(item)
# Return 1 if it is a video file
def isvideo(video):
    video_formats = ['.mp4', '.mkv', '.avi', '.mov', '.wmv']
    for video_format in video_formats:
        if video_format in video:
            tmp_video_format = video_format
            return True
    return False

# Return 1 if it is a subtitle file
def issub(sub):
    subs_formats = ['.srt', '.ass']
    for sub_format in subs_formats:
        if sub_format in sub:
            tmp_sub_format = sub_format
            return True
    return False

def get_video_format(video):
    video_formats = ['.mp4', '.mkv', '.avi', '.mov', '.wmv']
    for video_format in video_formats:
        if video_format in video:
            return video_format

def get_sub_format(sub):
    subs_formats = ['.srt', '.ass']
    for sub_format in subs_formats:
        if sub_format in sub:
            return sub_format

# rename a the subs list items to the videos list items's name
def rename(org_list, target_list):
    output_list = []
    for org_item, target_item in zip(org_list, target_list):
        tmp_video_format = get_video_format(target_item)
        tmp_sub_format = get_sub_format(org_item)
        target_item = target_item.replace(tmp_video_format, '')
        issub(org_item)
        org_item = target_item + tmp_sub_format 
        output_list.append(org_item)
    return output_list
