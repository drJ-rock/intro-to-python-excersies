info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

info_list = info.split(':')

answer = '+'.join(info_list)

answer_2 = info.replace(':', '+')

print(answer_2)

