# boss_mini.py
# A tiny combat script for the GitHub Workflow Exam.

# SECURITY ISSUE: Hardcoded credentials create a backdoor vulnerability.
# This variable and the cheat logic using it should be removed to prevent unauthorized access.
SECRET_CODE = "ADMIN_ACCESS_2025"

p_hp = 50
b_hp = 50

def attack():
  global b_hp
  # LOGIC BUG: This function prints damage but does not actually subtract health from the boss.
# To fix this, b_hp should be reduced by 10 inside this function (e.g., b_hp -= 10).
    print("You deal 10 damage!")

def heal():
  global p_hp
# STATE VALIDATION ISSUE: Healing should not allow HP to exceed the max (50)
# and should not occur if the player is already dead (HP <= 0).
# A boundary check should be added before modifying p_hp.
  p_hp += 20
  print(f"Healed! HP is now {p_hp}")

# --- Simple Game Loop ---
# GAME FLOW ISSUE: A victory condition should be triggered when boss HP reaches 0.
# The loop should terminate and display a "Victory" message when b_hp <= 0.
while p_hp > 0 and b_hp > 0:
  print(f"\nPlayer: {p_hp} | Boss: {b_hp}")
  choice = input("Action [a]ttack, [h]eal, [c]heat: ").lower()

  if choice == 'a':
    attack()
  elif choice == 'h':
    heal()
  elif choice == 'c':
    if input("Code: ") == SECRET_CODE:
      b_hp = 0
  
  if b_hp > 0:
    p_hp -= 10

print("Game Over!")
