import codegen


def main():
    parser = codegen.parser.register_parser()
    args = parser.parse_args()
    
    codegen.generate_file(framework=args.framework)


if  __name__ =='__main__':
    main()
