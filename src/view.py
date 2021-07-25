import utils

print('* ' + 'VIEW')

command = '''
CREATE VIEW credit_card_w_complaints AS
    SELECT * FROM credit_card_complaints
    WHERE consumer_complaint_narrative IS NOT NULL;
'''
utils.run_command(command, 'viewを作成する')
