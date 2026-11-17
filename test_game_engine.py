import pytest
from game_engine import Character, CharacterDeadError, InsufficientManaError

@pytest.fixture
def hero():
    return Character("Hero", hp=100, mana=50)

@pytest.fixture
def enemy():
    return Character("Enemy", hp=100, mana=0)

def test_bug_1_zero_hp_is_alive(hero):
    hero.take_damage(100) 
    assert hero.hp == 0
    assert hero.is_alive is False, "БАГ: Персонаж с 0 HP должен быть мёртв, но is_alive возвращает True!"

def test_bug_3_heal_exceeds_max_hp(hero):
    hero.take_damage(10)
    hero.heal(50) 
    assert hero.hp == 100, "БАГ: HP не должно превышать максимальное значение (max_hp)!"

def test_bug_4_poison_duration_decreases(enemy):
    enemy.status_effects["poison"] = 3 
    enemy.apply_turn_effects() 

    assert enemy.status_effects["poison"] == 2, "БАГ: Длительность яда должна уменьшаться каждый ход!"
