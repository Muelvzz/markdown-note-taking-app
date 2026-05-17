import "../css/dropdown.css"
import { Button } from "@/components/ui/button"
import { Empty, EmptyContent, EmptyDescription, EmptyHeader, EmptyMedia, EmptyTitle, } from "@/components/ui/empty"
import { Spinner } from "@/components/ui/spinner"

export default function DropdownInfo({ dropdownText }: { dropdownText: string }) {
  return (
    <div id="dropdown-card-container">
        <div id="dropdown-card">
            <Empty className="w-full">
            <EmptyHeader>
                <EmptyMedia variant="default">
                <Spinner className="size-8"/>
                </EmptyMedia>
                <EmptyTitle className="text-(--primary-color)">Processing your request</EmptyTitle>
                <EmptyDescription className="text-(--primary-color)">
                Please wait while we { dropdownText } your Note. Do not refresh the page.
                </EmptyDescription>
            </EmptyHeader>
            <EmptyContent>
                <Button variant="outline" size="sm" 
                    className="text-(--primary-color) border-(--primary-color)">
                Cancel
                </Button>
            </EmptyContent>
            </Empty>
        </div>

    </div>
  )
}
