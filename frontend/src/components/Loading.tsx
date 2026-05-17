import { Item, ItemContent, ItemMedia, ItemTitle, } from "@/components/ui/item"
import { Spinner } from "@/components/ui/spinner"

export default function Loading({ pageTitle }: { pageTitle: string }) {
  return (
    <article className="flex justify-center items-center min-h-screen">
        <div className="flex w-full max-w-xs flex-col gap-4 [--radius:1rem] text-(--primary-color)">
        <Item variant="muted">
            <ItemMedia>
            <Spinner />
            </ItemMedia>
            <ItemContent>
            <ItemTitle className="line-clamp-1">Loading { pageTitle } Page...</ItemTitle>
            </ItemContent>
        </Item>
        </div>
    </article>
  )
}
