def init_consts():
    code = "_=+({}=={});"
    for i in range(2, 5 + 1): code += f"{'_'*i}={'_'*(i-1)}+_;"
    return code

def main():
    str_list = [
        '_____ * ((___ * __ + _) * __)',
        '((_____ * __) * (___ * ___)) + ___ * __ + _',
        '((_____ * __) * ((___ * ___ + __)))',
        '((__ + ___) * ((___ * ___ + _) * __ + _))',
        '(__ * __ * __ * __ * __)',
        '(__ + ___) * ((___ + __ )* ___)',
        '((_____ * __) * (___ * ___)) + ___ * __ + _',
        '(_____ + _) * (_____ * ___ + __)',
        '((_____ * __) * (___ * ___)) + ___ * __ + _',
        '(__ * __ * __ * __ * __)',
        '__ * ((_____ * __) * _____ + ___)',
        '(__ * _____) * (__ * _____) + _',
        '(__ * __ * __ * __ * __)',
        '((_____ * __) * ((___ * ___ + __)))',
        '((_____ * __) * (___ * ___)) + ___ * __ + _',
        '__ * ((_____ * __) * _____ + ___)',
        '((_____ * __) * (___ * ___)) + ___ * __ + __',
        '((_____ * __) * ((___ * ___ + __))) + _',
        '((__ + ___) * ((___ * ___ + _) * __ + _)) + ___',
        '__ * ((_____ * __) * _____ + ___)',
        '((_____ * __) * (___ * ___)) + ___ * __ + _',
        '(__ * __ * __ * __ * __) + _',
        ]

    str_list_len = len(str_list)
    code = init_consts()
    code += f"""exec((('%'+'\143')*({str_list_len}))%({','.join(str_list)}));"""
    exec(code)

if __name__ == "__main__":
    main()
