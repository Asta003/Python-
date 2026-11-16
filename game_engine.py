class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    RESET = "\033[0m"
    BOLD = "\033[1m"


class CharacterDeadError(Exception): pass
class InsufficientManaError(Exception): pass


class Character:
    def __init__(self, name: str, hp: int = 100, mana: int = 50):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mana = mana
        self.mana = mana
        self.status_effects = {}

    @property
    def is_alive(self) -> bool:
        return self.hp >= 0

    def render_bar(self, current: int, max_val: int, color: str, length: int = 10) -> str:
        if max_val <= 0:
            ratio = 0
        else:
            ratio = max(0, min(1, current / max_val))

        filled = int(length * ratio)
        bar = "█" * filled + "░" * (length - filled)
        return f"{color}[{bar}] {current}/{max_val}{Colors.RESET}"

    def get_status_card(self) -> str:
        hp_bar = self.render_bar(self.hp, self.max_hp, Colors.GREEN)
        mana_bar = self.render_bar(self.mana, self.max_mana, Colors.BLUE)
        status = f" {Colors.RED}☠️ POISONED{Colors.RESET}" if "poison" in self.status_effects else ""
        return (
            f"{Colors.BOLD}{self.name}{Colors.RESET}\n"
            f"   HP:   {hp_bar}\n"
            f"   MANA: {mana_bar}"
        )

    def take_damage(self, damage: int) -> int:
        if not self.is_alive:
            raise CharacterDeadError(f"{self.name} уже мёртв!")

        self.hp = self.hp - damage
        return damage

    def heal(self, amount: int) -> int:
        if not self.is_alive:
            raise CharacterDeadError("Нельзя вылечить мёртвого!")
        
        old_hp = self.hp
        self.hp = self.hp + amount
        return self.hp - old_hp

    def cast_spell(self, spell_name: str, target: 'Character' = None) -> str:
        if not self.is_alive:
            raise CharacterDeadError("Мёртвый не может колдовать!")

        spells = {
            "sword_attack": {"mana": 0, "damage": 15, "icon": "⚔️ УДАР МЕЧОМ"},
            "fireball": {"mana": 20, "damage": 35, "icon": "🔥 FIREBALL"},
            "heal": {"mana": 15, "heal": 30, "icon": "✨ HEAL"},
            "poison_dart": {"mana": 10, "damage": 10, "effect": "poison", "icon": "☠️ POISON DART"}
        }

        if spell_name not in spells:
            raise ValueError(f"Заклинание {spell_name} не найдено")

        spell = spells[spell_name]
        if self.mana < spell["mana"]:
            raise InsufficientManaError("Недостаточно маны!")

        self.mana -= spell["mana"]

        if "damage" in spell:
            if not target:
                raise ValueError("Нужна цель для атаки!")
            target.take_damage(spell["damage"])
            if "effect" in spell:
                target.status_effects[spell["effect"]] = 3
            return f"{Colors.YELLOW}{spell['icon']}{Colors.RESET} от {self.name} бьёт {target.name}!"
        elif "heal" in spell:
            healed = self.heal(spell["heal"])
            return f"{Colors.CYAN}{spell['icon']}{Colors.RESET}: {self.name} восстановил +{healed} HP!"

    def apply_turn_effects(self) -> list:
        logs = []
        if not self.is_alive:
            return logs

        if "poison" in self.status_effects and self.status_effects["poison"] > 0:
            self.take_damage(10)
            logs.append(f"{self.name} получает 10 урона от яда!")
        return logs