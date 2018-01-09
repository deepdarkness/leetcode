class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        chars.append('*')
        self.l = len(chars)
        if self.l == 0:
            return 0

        pre_letter = chars[0]
        letter_amount = 1
        write_pos = 0
        for ptr in range(1, self.l):
            now_letter = chars[ptr]
            if now_letter == pre_letter:
                letter_amount += 1
            else:
                if letter_amount == 1:
                    self.input_letter(write_pos, chars, pre_letter)
                    write_pos += 1
                    pre_letter = now_letter
                    continue
                else:
                    input_str = pre_letter + str(letter_amount)
                    self.input_letter(write_pos, chars, input_str)
                    write_pos += len(input_str)
                    pre_letter = now_letter
                    letter_amount = 1
        return write_pos

    def input_letter(self, pos, chars, input_str):
        for i in input_str:
            if pos < len(chars):
                chars[pos] = i
            else:
                chars.append(i)
            pos += 1
