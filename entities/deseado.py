class Deseado:
    def __init__(self, name, image, link, text, video):
        self.name = name
        self.image = image
        self.link = link
        self.text = text
        self.video = video
    
    @classmethod
    def get_list(cls):
        deseados = [
            cls("DRAGON QUEST III HD-2D Remake", 
                "https://m.media-amazon.com/images/M/MV5BODg5MzMwMDgtNTVkYy00YTI1LWIwOTAtMDlmOWEwNDliMzUzXkEyXkFqcGc@._V1_.jpg",
                "https://store.steampowered.com/app/2701660/DRAGON_QUEST_III_HD2D_Remake/",
                "Lo quiero porque me empecé a jugar los originales y me emociona mucho verlo con tecnología mucho mas moderna y contenido nuevo!!",
                "https://www.youtube.com/embed/1ltsk99E-RY?si=w92p02v8wlRk1qEv"),
            cls("Persona 3 Reload",
                "https://preview.redd.it/the-box-art-for-persona-3-reload-v0-gl0jcz2p9tjb1.jpg?width=640&crop=smart&auto=webp&s=fb6d0b6aae168f87daf7bb52317d1a842ffac421",
                "https://store.steampowered.com/app/2161700/Persona_3_Reload/",
                "Lo quiero pq me gustan mucho los personas, pero, no lo comprare hasta que me termine el 5.",
                "https://www.youtube.com/embed/DG_gy1Tecco?si=12K7pGVTP8--c18s"),
            cls("Professor Layton and The New World of steam",
                "https://gamefaqs.gamespot.com/a/box/2/7/5/1131275_front.jpg",
                "https://www.nintendo.com/es-mx/store/products/professor-layton-and-the-new-world-of-steam-switch/?srsltid=AfmBOory-MuCUegwodRx1ItxsxZH1aPKLmQcy_pDeY9nN9sEBniVY5ct",
                "Aun no sale pero lo quiero porque me gustan mucho los juegos de puzzles y professor layton es de mis sagas favoritaas!! Amo todo de ellos, en especial la musica.",
                "https://www.youtube.com/embed/9Sj0BXBNugQ?si=F0QabTEeOTqvjSo2"),
            cls("Steins;Gate 0",
                "https://external-preview.redd.it/-ggECo27XKcLFA2hdu-Q-FIm_8LqAeiCBRoRSRbh1r4.jpg?width=1080&crop=smart&auto=webp&s=91cf43649dd25029659544c8db0ed95ae14e2153",
                "https://store.steampowered.com/app/825630/STEINSGATE_0/",
                "Me encantan los juegos que son principalmente historia. Jugué el primero y me volo la mente, así que quiero saber qué sucede en esta secuela, y mas aún pq es de viajes en el tiempo + amor tragico.",
                "https://www.youtube.com/embed/ZHh-WR0Eu-g?si=xY7xWzimpkC5KjsG"),
                
        ]
        return deseados

        