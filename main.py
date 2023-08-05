import data_manage

if data_manage.journal_done():
    print("You have already completed your journal for today.")
else:
    import journal
    journal.main()