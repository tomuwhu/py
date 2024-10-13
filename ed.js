function levenshtein(s1, s2) {
      l1 = s1.length
      l2 = s2.length
      matrix = [Array(range(l1 + 1))] * (l2 + 1)
      for (zz=0; zz <= l2; zz++){
        matrix[zz] = list(range(zz,zz + l1 + 1))
      }
      for zz in list(range(0,l2)):
        for sz in list(range(0,l1)):
          if s1[sz] == s2[zz]:
            matrix[zz+1][sz+1] = min(matrix[zz+1][sz] + 1, matrix[zz][sz+1] + 1, matrix[zz][sz])
          else:
            matrix[zz+1][sz+1] = min(matrix[zz+1][sz] + 1, matrix[zz][sz+1] + 1, matrix[zz][sz] + 1)
      distance = int(float(matrix[l2][l1]))
      return distance
}
console.log(levenshtein(input(),input()))
