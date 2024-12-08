import time


class User:
    def __init__(self, nickname, password,age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
    def get_info(self):
        return self.nickname, self.password
    def __str__(self):
         return self.nickname
    def __eq__(self,other):
        return self.nickname == other.nickname

class Video:
    def __init__(self, title, duration,adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, login, password):
        for user in self.users:
            if (login, hash(password)) == User.get_info():
                self.current_user = user
                return user

    def register(self, nickname, password, age):
        new_user = User(nickname, password, age)
        if new_user not in self.users:
           self.users.append(new_user)
           print('Такого пользователя нет')
           self.current_user = new_user
        else:
            print(f'Пользователь {self.current_user} с таким логином существует')

    def log_out(self):
        self.current_user = None

    def add(self, *videos: Video):
        for video in videos:
            if video.title not in self.videos:
                self.videos.append(video)

    def get_videos(self, search):
        titles=[]
        for video in self.videos:
            if search.lower() in str(video).lower():
                titles.append(video)
        return titles

    def watch_video(self,title):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть')
            return
        else:
            for video in self.videos:
                if title == video.title:
                    if video.adult_mode and self.current_user.age >=18:
                        while video.time_now < video.duration:
                            video.time_now +=1
                            print(video.time_now, end=' ')
                            time.sleep(1)
                        video.time_now = 0
                        print('Конец видео')
                    else:
                        print('Вам нет 18 лет')
                    break



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode = True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
#
# # Проверка на вход пользователя и возрастное ограничение
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('vasya_pupkin', 'lolkekcheburek', 13)
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
# ur.watch_video('Для чего девушкам парень программист?')
#
# # Проверка входа в другой аккаунт
# ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
# print(ur.current_user)
# # Попытка воспроизведения несуществующего видео
#
# ur.watch_video('Лучший язык программирования 2024 года!')
#
#
#
#


