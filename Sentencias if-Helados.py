# Imaginemos que quieres comprar un helado para 10 de tus amigos
# Escribe un programa que tome el dinero que tienes y el precio de un helado y que saca el dinero restante solo si puedes comprar ese helado para tus 10 amigos

dinero=int(input())
precio=int(input())
total=10*precio
resto=dinero-total

if dinero>=total:
    print(resto)
