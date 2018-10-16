import base64
import os
import pickle

from utils import printmd


class Helper:
    def __init__(self, backup_filename=None):
        if backup_filename is None:
            backup_filename = 'utils/.hints_taken'
        self.backup_filename = backup_filename
        self.hints_taken = self._load_hints_taken()
        
    def _load_hints_taken(self):
        if os.path.exists(self.backup_filename):
            with open(self.backup_filename, 'r') as f:
                content = f.read()
            hints_taken = set(content.split())
        else:
            hints_taken = set([])
        return hints_taken
            
    def _save_hints_taken(self):
        with open(self.backup_filename, 'w') as f:
            f.write('\n'.join(self.hints_taken))
            
    def reset(self):
        if os.path.exists(self.backup_filename):
            os.remove(self.backup_filename)

    def get_hint_msg(self, exercise):
        filename = 'utils/.data/{}.pkl'.format(exercise)
        if os.path.exists(filename):
            with open(filename, 'rb') as f:
                hint_msg = pickle.load(f)
            hint_msg = base64.b64decode(hint_msg).decode('utf-8')
            self.hints_taken.add(exercise)
            self._save_hints_taken()
        else:
            hint_msg = 'Não há dicas! A sabedoria está em você!'
        return hint_msg
    
    def get_usage(self):
        hints_taken = self._load_hints_taken()
        count = len(hints_taken)
        maybe_s = '' if count == 1 else 's'
        printmd('Você usou dicas em {} exercício{}.'.format(count, maybe_s))
        if count == 0:
            printmd('Uau, parabéns por ter conseguido fazer os exercícios sem dicas!')
        else:
            printmd('Os exercícios que você usou minha ajudinha foram:')
            printmd('* {}'.format('\n* '.join(hints_taken)))


def give_me_a_hint(exercise):
    hint_msg = Helper().get_hint_msg(exercise)
    printmd(hint_msg)   