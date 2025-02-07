"""Step1

�l�@�F
�E ���ꂼ��̕�����ɑ΂��āC�����̌����������鎫�������C�����������o���オ�邩�ǂ������ׂ�D

���ȁF
�E��̕�������\�[�g���Ĕ�r������@���̂ĂĂ��܂��Ă����D

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_to_count = {}

        for c in s:
            if c not in char_to_count:
                char_to_count[c] = 1
                continue
            char_to_count[c] += 1

        for c in t:
            if c not in char_to_count:
                return False
            char_to_count[c] -= 1

        for key, value in char_to_count.items():
            if value != 0:
                return False
        
        return True