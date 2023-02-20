def list_of_menu_functions():
    print("""
    1. Phone book
    2. Messages
    3. Chat
    4. Call register
    5. Tones
    6. Settings
    7. Call divert
    8. Games
    9. Calculator
    10. Reminders
    11. Clock
    12. Profiles
    13. SIM services
    """)


def phone_book_menu():
    print("""
    1. Search
    2. Service Nos.
    3. Add name
    4. Erase
    5. Edit
    6. Assign tone
    7. Send b'card
    8. Options
    9. Speed dials
    10. Voice tags
    
    0. Exit
    """)


def messages_menu():
    print("""
    1. Write messages
    2. Inbox
    3. Outbox
    4. Picture messages
    5. Templates
    6. Smileys
    7. Message settings
    8. Info service
    9. Voice mailbox number
    10. Service command editor
    
    0. Exit
    """)


def chat_menu():
    print("""
     Chat
     
     0. Exit
    """)


def call_register_menu():
    print("""
    1. Missed calls
    2. Received calls
    3. Dialled numbers
    4. Erase recent call lists
    5. Show call duration
    6. Show call costs
    7. Call cost settings
    8. Prepaid credit
    
    0. Exit
    """)


def tones_menu_function():
    print("""
    1. Ringing tone
    2. Ringing volume
    3. Incoming call alert
    4. Composer
    5. Message alert tone
    6. Keypad tones
    7. Warning and game tones
    8. Vibrating alert
    9. Screen saver
    
    0. Exit
    """)


def settings_menu_function():
    print("""
    1. Call settings
    2. Phone settings
    3. Security settings
    4. Restore factory settings
    
    0. Exit
    """)


def call_divert_menu_function():
    print("""
    Call divert
    
    0. Exit
    """)


def games_menu_function():
    print("""
    Games
    
    0 Exit
    """)


def calculator_menu_function():
    print("""
    Calculator
    
    0. Exit
    """)


def reminders_menu_function():
    print("""
    Reminders
    
    0. Exit
    """)


def clock_menu_function():
    print("""
    Clock
    
    0. Exit
    """)


def profiles_menu_function():
    print("""
    Profiles
    
    0. Exit
    """)


def sim_services_menu():
    print("""
    SIM services
    
    0. Exit
    """)


user_input = int(input("Enter number: "))

match user_input:
    case 1:
        phone_book_menu()
