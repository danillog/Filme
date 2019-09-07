# -*- coding: cp1252 -*-
import fresh_tomatoes
import media

toy_story = media.Movie( "Toy Story",
                                        "A histoória de um garoto e seus brinquedos",
                                        "https://upload.wikimedia.org/wikipedia/pt/d/dc/Movie_poster_toy_story.jpg",
                                        "https://www.youtube.com/watch?v=KYz2wyBy3kc" )
#print(toy_story.story)

avatar = media.Movie("Avatar",
                                    " Planeta alienigena",
                                     "https://uauposters.com.br/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/1/5/156820140525-uau-posters-filmes-avatar.jpg",
                                    "https://www.youtube.com/watch?v=d1_JBMrrYw8")
#avatar.show_trailer()

xuxa = media.Movie("Xuxa e os Duendes 2",
                               "Xuxa  no caminho das fadas",
                               "https://upload.wikimedia.org/wikipedia/pt/6/6b/Dvd-xuxa-e-os-duendes-2.jpg",
                               "https://www.youtube.com/watch?v=3zLgjVRha4Y")



hamburguer = media.Movie("Ta chovendo Hamburguer",
                                             "Prepara-se para um banquete",
                                             "https://http2.mlstatic.com/dvd-ta-chovendo-hamburguer-D_NQ_NP_958122-MLB26646446582_012018-F.jpg",
                                             "https://www.youtube.com/watch?v=egeE-0aMiBs")


movies = [toy_story, avatar, xuxa, hamburguer]
fresh_tomatoes.open_movies_page(movies)


                               
