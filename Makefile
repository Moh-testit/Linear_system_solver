##
## EPITECH PROJECT, 2021
## B-MAT-500-COT-5-1-306radiator-mohamed.mazu
## File description:
## Makefile
##

NAME	=	306radiator

all:	$(NAME)

$(NAME):
		ln -s 306radiator.py $(NAME)
		chmod +x $(NAME)

clean:
		rm -rf *~
		rm -rf __pycache__

fclean:	clean
		rm -rf $(NAME)

re:	fclean all