from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

lst = ['1','2','3','4','5','6','7','8','9' ]
lst1 = []
lst2 = []
lst3 = []
win = -1
player = 1
countt_turn = 0

def prn_lst(lst):
    lst2 = 'ходит  игрок ' + str(player) + '\n\n' + lst[0] + '  ' + lst[1] + '  ' + lst [2] + '\n' + \
    lst[3] + '  ' + lst[4] + '  ' + lst [5] + '\n' + lst[6] + '  ' + lst[7] + '  ' + lst [8] + '\n'
    return lst2

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(prn_lst(lst))
async def h1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if check_win(lst, 0) > 0:
        await update.message.reply_text(f'{prn_lst(lst)} \n выиграл игрок {player} !!!!!!!!')
    elif check_win(lst, 0) == 0:
        await update.message.reply_text(f'{prn_lst(lst)} \n ничья !!!!!!!!')
    else: await update.message.reply_text(prn_lst(lst))    
async def h2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if check_win(lst, 1) > 0:
        await update.message.reply_text(f'{prn_lst(lst)} \n выиграл игрок {player} !!!!!!!!')
    elif check_win(lst, 1) == 0:
        await update.message.reply_text(f'{prn_lst(lst)} \n ничья !!!!!!!!')
    else: await update.message.reply_text(prn_lst(lst))
async def h3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if check_win(lst, 2) > 0:
        await update.message.reply_text(f'{prn_lst(lst)} \n выиграл игрок {player} !!!!!!!!')
    elif check_win(lst, 2) == 0:
        await update.message.reply_text(f'{prn_lst(lst)} \n ничья !!!!!!!!')
    else: await update.message.reply_text(prn_lst(lst))
async def h4(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if check_win(lst, 3) > 0:
        await update.message.reply_text(f'{prn_lst(lst)} \n выиграл игрок {player} !!!!!!!!')
    elif check_win(lst, 3) == 0:
        await update.message.reply_text(f'{prn_lst(lst)} \n ничья !!!!!!!!')
    else: await update.message.reply_text(prn_lst(lst))
async def h5(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if check_win(lst, 4) > 0:
        await update.message.reply_text(f'{prn_lst(lst)} \n выиграл игрок {player} !!!!!!!!')
    elif check_win(lst, 4) == 0:
        await update.message.reply_text(f'{prn_lst(lst)} \n ничья !!!!!!!!')
    else: await update.message.reply_text(prn_lst(lst))
async def h6(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if check_win(lst, 5) > 0:
        await update.message.reply_text(f'{prn_lst(lst)} \n выиграл игрок {player} !!!!!!!!')
    elif check_win(lst, 5) == 0:
        await update.message.reply_text(f'{prn_lst(lst)} \n ничья !!!!!!!!')
    else: await update.message.reply_text(prn_lst(lst))
async def h7(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if check_win(lst, 6) > 0:
        await update.message.reply_text(f'{prn_lst(lst)} \n выиграл игрок {player} !!!!!!!!')
    elif check_win(lst, 6) == 0:
        await update.message.reply_text(f'{prn_lst(lst)} \n ничья !!!!!!!!')
    else: await update.message.reply_text(prn_lst(lst))
async def h8(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if check_win(lst, 7) > 0:
        await update.message.reply_text(f' {prn_lst(lst)} \n выиграл игрок {player} !!!!!!!!')
    elif check_win(lst, 7) == 0:
        await update.message.reply_text(f'{prn_lst(lst)} \n ничья !!!!!!!!')
    else: await update.message.reply_text(prn_lst(lst))
async def h9(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if check_win(lst, 8) > 0:
        await update.message.reply_text(f'{prn_lst(lst)} \n выиграл игрок {player} !!!!!!!!')
    elif check_win(lst, 8) == 0:
        await update.message.reply_text(f'{prn_lst(lst)} \n ничья !!!!!!!!')
    else: await update.message.reply_text(prn_lst(lst))

app = ApplicationBuilder().token("5753604058:AAHLeZ1vZfdB6kJDd7TW64DwrLJybb9fpHo").build()
app.add_handler(CommandHandler("hello", hello))

def check_win(lst, index_num):
    if lst [index_num].isdigit(): 
        global player, countt_turn, win
        countt_turn += 1
        if player == 1:
            lst [index_num] = 'X'
        else:
            lst [index_num] = 'O'
        if lst[0] == lst[1] and lst[1] == lst[2] or \
        lst[3] == lst[4] and lst[4] == lst[5] or \
        lst[6] == lst[7] and lst[7] == lst[8] or \
        lst[0] == lst[3] and lst[3] == lst[6] or \
        lst[1] == lst[4] and lst[4] == lst[7] or \
        lst[2] == lst[5] and lst[5] == lst[8] or \
        lst[0] == lst[4] and lst[4] == lst[8] or \
        lst[2] == lst[4] and lst[4] == lst[6]:
            if player == 1: 
                return (2)
            elif player == 2: 
                return (1)
        elif countt_turn > 8: 
            return (0)
        if player == 1: 
            player += 1
        else: 
            player -= 1
        return (-1)
    return (-1)   
app.add_handler(MessageHandler(filters.Text('1'), h1))
app.add_handler(MessageHandler(filters.Text('2'), h2))
app.add_handler(MessageHandler(filters.Text('3'), h3))
app.add_handler(MessageHandler(filters.Text('4'), h4))
app.add_handler(MessageHandler(filters.Text('5'), h5))
app.add_handler(MessageHandler(filters.Text('6'), h6))
app.add_handler(MessageHandler(filters.Text('7'), h7))
app.add_handler(MessageHandler(filters.Text('8'), h8))
app.add_handler(MessageHandler(filters.Text('9'), h9))
app.run_polling()
