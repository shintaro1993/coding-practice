"""Step2

�l�@�F
�E ���ꂼ��̕�����ɑ΂��āC�����̌����������鎫�������C�����������o���オ�邩�ǂ������ׂ�D

���ȁF
�E��̕�������\�[�g���Ĕ�r������@���̂ĂĂ��܂��Ă����D

"""

class Solution:
    def make_letter_to_count_dict(s):
        letter_to_count = {}
        for c in s:
            if c not in letter_to_count:
                letter_to_count[c] = 1
                continue
            letter_to_count[c] += 1
        return letter_to_count

    def isAnagram(self, s: str, t: str) -> bool:
        return make_letter_to_count(s) == make_letter_to_count(t)


