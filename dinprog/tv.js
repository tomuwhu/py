let o = {
    mi(i = 0, j = this.s.length - 1) {
        return this.t[i][j] ? this.t[i][j] : i >= j ? this.t[i][j] = 1 :
            this.s[i] === this.s[j] ? this.t[i][j] = this.mi(i + 1, j - 1) :
                this.t[i][j] = Math.min(this.mi(i + 1, j), this.mi(i, j - 1)) + 1
    },
    mo(i = 0, j = this.s.length - 1) {
        let s = this.s.split('')
        do this.t[i][j - 1] + 1 === this.t[i][j] ? s[j--] = '.' :
            this.t[i + 1][j] + 1 === this.t[i][j] ? s[i++] = '.' : (i++, j--)
        while (this.t[i][j] - 1)
        return s.join('')
    }
}