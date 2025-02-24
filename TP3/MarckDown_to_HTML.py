import sys
import re


def convert_lines(lines:list[str])-> str:
    """Converts a list of markdown lines to HTML."""
    html_lines = []
    inside_ol = False 
    
    for line in lines:
    
        # Headers 
        if re.match(r"^###\s+(.+)", line):
            html_lines.append(re.sub(r"^###\s+(.+)", r"<h3>\1</h3>", line))
            continue
        if re.match(r"^##\s+(.+)", line):
            html_lines.append(re.sub(r"^##\s+(.+)", r"<h2>\1</h2>", line))
            continue
        if re.match(r"^#\s+(.+)", line):
            html_lines.append(re.sub(r"^#\s+(.+)", r"<h1>\1</h1>", line))
            continue

        # Bold and Italic
        line = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", line)
        line = re.sub(r"\*(.*?)\*", r"<i>\1</i>", line)

        # Images and Links
        line = re.sub(r"\!\[(.*?)\]\((.*?)\)", r"<img src='\2' alt='\1'>", line)
        line = re.sub(r"\[(.*?)\]\((.*?)\)", r"<a href='\2'>\1</a>", line)

        # Ordered List
        if re.match(r"^\d+\.\s+.+", line):
            if not inside_ol:
                html_lines.append("<ol>")  
                inside_ol = True
            html_lines.append(re.sub(r"^\d+\.\s+(.+)", r"<li>\1</li>", line))
            continue
        else:
            if inside_ol:
                html_lines.append("</ol>")  
                inside_ol = False

        html_lines.append(line)

    if inside_ol:
        html_lines.append("</ol>")  

    return "\n".join(html_lines)


def main() -> None:
    if len(sys.argv) == 1:
        print("Usage: python MarckDown_to_HTML.py <file_path> [<output_path>]")
        return
    
    file_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None


    if output_path is None: 
        file_path = sys.argv[1]
        try:
            with open(file_path, "r") as file:
                lines= [line.rstrip() for line in file]
                print(convert_lines(lines))

        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return
            
    elif output_path is not None:
        file_path = sys.argv[1]
        print(f"File path: {file_path}")
        output_path = sys.argv[2]
        print(f"Output path: {output_path}")
        try:
            with open(file_path, "r") as file:
                lines= [line.rstrip() for line in file]
                with open(output_path, "w") as output_file:
                    output_file.write(convert_lines(lines))
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return



if __name__ == "__main__":
    main()