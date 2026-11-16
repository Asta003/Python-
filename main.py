import os
import time
from game_engine import Character, Colors


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def play_game():
    hero = Character("🤖 Кибер-чумба", hp=100, mana=50)
    boss = Character("🕷️ Павук", hp=120, mana=0)

    while hero.is_alive and boss.is_alive:
        clear_screen()
        print(f"{Colors.CYAN}=== ПОШАГОВАЯ АРЕНА ==={Colors.RESET}\n")
        print(hero.get_status_card())
        print("-" * 35)
        print(boss.get_status_card())
        print("-" * 35)

        print("\nВыберите действие:")
        print("1. 🔪 Резня (0 MP / 15 DMG)")
        print("2. 🔥 Огненный плевок (20 MP / 35 DMG)")
        print("3. 🧪 Лечение (15 MP / +30 HP)")
        print("4. ☠️ Столбняковый гвоздь (10 MP / 10 DMG + Яд)")

        choice = input("\nВаш ход (1-4): ")

        try:
            if choice == "1":
                log = hero.cast_spell("sword_attack", target=boss)
            elif choice == "2":
                log = hero.cast_spell("fireball", target=boss)
            elif choice == "3":
                log = hero.cast_spell("heal")
            elif choice == "4":
                log = hero.cast_spell("poison_dart", target=boss)
            else:
                log = "Пропуск хода..."

            print(f"\n{log}")

            boss.apply_turn_effects()
            if boss.is_alive:
                dmg = hero.take_damage(20)
                print(f"{Colors.RED}👾 Босс наносит {dmg} урона!{Colors.RESET}")

            time.sleep(2)

        except Exception as e:
            print(f"\n{Colors.RED}Ошибка: {e}{Colors.RESET}")
            time.sleep(1.5)

    clear_screen()
    if hero.is_alive:
        print(f"{Colors.GREEN}🎉 ПОБЕДА! {hero.name} уничтожил босса!{Colors.RESET}")
    else:
        print(f"{Colors.RED}💀 ПОТРАЧЕНО! {hero.name} пал в бою.{Colors.RESET}")


if __name__ == "__main__":
    play_game()
