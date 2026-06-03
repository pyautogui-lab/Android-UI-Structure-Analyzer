import re
from dataclasses import dataclass


@dataclass
class UIElement:
    resource_id: str
    left: int
    top: int
    right: int
    bottom: int

    @property
    def center(self):
        x = (self.left + self.right) // 2
        y = (self.top + self.bottom) // 2
        return x, y


def extract_elements(xml_text: str, target_resource_id: str):
    pattern = (
        rf'resource-id="{re.escape(target_resource_id)}".+?'
        r'bounds="\[([0-9]+),([0-9]+)\]\[([0-9]+),([0-9]+)\]"'
    )

    matches = re.findall(
    pattern,
    xml_text,
    re.DOTALL
    )

    elements = []
    for left, top, right, bottom in matches:
        elements.append(
            UIElement(
                resource_id=target_resource_id,
                left=int(left),
                top=int(top),
                right=int(right),
                bottom=int(bottom),
            )
        )

    return elements


def main():
    xml_path = "sample_window_dump.xml"
    target_resource_id = "sample.app:id/target_button"

    with open(xml_path, "r", encoding="utf-8") as file:
        xml_text = file.read()
    

    elements = extract_elements(xml_text, target_resource_id)

    if not elements:
        print("Target UI element was not found.")
        return

    for index, element in enumerate(elements, start=1):
        x, y = element.center
        print(f"[{index}] resource-id: {element.resource_id}")
        print(f"    bounds: ({element.left}, {element.top}) - ({element.right}, {element.bottom})")
        print(f"    center: ({x}, {y})")


if __name__ == "__main__":
    main()