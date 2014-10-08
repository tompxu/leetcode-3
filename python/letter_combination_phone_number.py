class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        code = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
        output = []
        def permute(index, result, output):
            if index == len(digits):
                output.append(result)
                return
            else:
                for x in code[digits[index]]:
                    permute(index+1, result+x, output)
        permute(0,"", output)
        return output