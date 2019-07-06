import catchWeb
import mysqlAction

if __name__ == "__main__":
    # https://facejav.com/page/2/
    # pageUrl = 'https://facejav.com'
    fj_list = catchWeb.init('https://facejav.com')
    
    mysqlAction.initSave(fj_list)


