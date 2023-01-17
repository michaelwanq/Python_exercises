# 练习 8-8：用户的专辑
# 在为完成练习 8-7 编写的程序中，编写一个 while 循环，让用户输入专辑的歌手和名称。
# 获取这些信息后，使用它们来调用函数 make_album()并将创建的字典打印出来。在这个 while 循环中，务必提供退出途径。
# def make_album(singer_name, album_name, song_number=''):
#     if song_number:
#         s_a = {'singer_name': singer_name, 'album_name': album_name, 'song_number': song_number}
#     else:
#         s_a = {'singer_name': singer_name, 'album_name': album_name}
#     return s_a
# while True:
#     print('请输入歌手的名字、专辑、歌曲数量！')
#     singer_name = input('请输入歌手的名字:')
#     print(singer_name)
#     album_name = input('请输入专辑的名称:')
#     print(album_name)
#     song_number = input('请输入专辑的歌曲数量：')
#     print(song_number)
#     if (singer_name != 'q') and (album_name != 'q'):
#         a = make_album(singer_name, album_name, song_number)
#         print(a)
#     else:
#         print('感谢使用，再见！')
#         break


def make_album(artist, title, tracks=0):
    """创建一个包含专辑信息的字典。"""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
    }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict


# 生成提示语。
title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who's the artist? "
tracks_prompt = "How many tracks in th album?"
# 让用户知道如何退出。
print("Enter 'q' at any time to stop.")
while True:
    title = input(title_prompt)
    if title == 'q':
        break

    artist = input(artist_prompt)
    if artist == 'q':
        break
    tracks = input(tracks_prompt)
    if artist == 'q':
        break

    album = make_album(artist, title,tracks)
    print(album)
print("\nThanks for responding!")
