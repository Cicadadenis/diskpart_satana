def show_command_buttons():
    for widget in commands_frame.winfo_children():
        widget.destroy()

    commands = [
        ("select disk", f"select disk {selected_disk}", "Выбрать диск для работы"),
        ("clean", "clean", "Удалить все разделы на диске"),
        ("convert GPT", "convert gpt", "Конвертировать диск в GPT"),
        ("convert MBR", "convert mbr", "Конвертировать диск в MBR"),
        ("create partition primary", "create partition primary", "Создать основной раздел"),
        ("create partition efi 300MB", "create partition efi size=300", "Создать EFI раздел 300 МБ"),
        ("create partition msr 16MB", "create partition msr size=16", "Создать MSR раздел 16 МБ"),
        ("format NTFS", f"format fs=ntfs quick label=Disk{selected_disk}", "Форматировать в NTFS"),
        ("format FAT32", f"format fs=fat32 quick label=EFI", "Форматировать в FAT32"),
        ("assign letter", f"assign letter=S", "Назначить букву S"),
        ("shrink 800MB", "shrink desired=800", "Уменьшить размер раздела на 800 МБ"),
        ("list volume", "list volume", "Показать все тома"),
        ("detail disk", "detail disk", "Показать информацию о выбранном диске"),
        ("exit", "exit", "Выйти из diskpart"),
        ("Разметка WIN", "full_script", "Создание EFI, MSR, Windows и Recovery разделов")
    ]

    for i, (label, cmd, desc) in enumerate(commands):
        btn = tk.Button(
            commands_frame, text=label, width=20, bg="#202437", fg="#d0c8ff",
            activebackground="#3c4370", relief="flat",
            command=lambda c=cmd: run_full_script() if c=="full_script" else run_diskpart([f"select disk {selected_disk}", c])
        )
        row = i // 3
        col = i % 3
        btn.grid(row=row, column=col, padx=5, pady=5)
        CreateToolTip(btn, desc)
