import time
class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None   # т.к. пока его не существует

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and hash(password) ==  user.password: # как прописать, если поль-ль с логином и паролем существует?
                 self.current_user = user

    def register(self, nickname, password, age):
        new_user = User(nickname, password, age) # создали объект класса User
        if new_user not in self.users:
            self.users.append(new_user)               # потом добавили его в пользователя
            self.current_user = new_user              # зарегистрированный польз-ль стал текущим пользователем
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self): # метод для сброса текущего пользователя на None
        self.current_user = None

    def add(self, *videos):  # метод, который принимает неогр. кол-во объектов класса Video  и добавляет их в videos
        for video in videos:
            if video.tittle not in self.videos: #
                self.videos.append(video)

    def get_videos(self, search_word):
        list_tittle = []
        for video in self.videos:
            if search_word.lower() in str(video).lower(): # страховка, вдруг введем число
                list_tittle.append(video)
        return list_tittle

    def watch_video(self, tittle_videos):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return # чтобы возвращался объект, если не вошли в аккаунт, то не можем смотреть дальше видео
        for video in self.videos:
            if tittle_videos == video.tittle: #
                if self.current_user.age >= 18 and video.adult_mode: # как прописать ограничение по возрасту?
                    while video.time_now < video.duration:
                        video.time_now += 1
                        print(video.time_now, end=" ")  # необязательный параметр, который разделяет принты пробелом
                        time.sleep(1)
                    video.time_now = 0 # чтобы следующее видео началось с начала
                    print("Конец видео")
                else:
                     print("Вам нет 18 лет, пожалуйста, покиньте страницу")
                break # чтобы выбрасывало из цикла, если неподходящий возраст


class Video:
    def __init__(self, tittle, duration, adult_mode = False):
        self.tittle = tittle
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return self.tittle
    def __repr__(self):
        return self.tittle



class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname
    def __eq__(self, other):
         return self.nickname == other.nickname

ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)

v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)



# Добавление видео
ur.add(v1, v2)
# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')