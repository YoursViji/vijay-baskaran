import type { ReactNode } from "react";
import Image from "next/image";
import {
  ArrowUpRight,
  FileText,
  Mail,
  MapPin,
  Phone,
  Sparkles,
} from "lucide-react";

import { Badge } from "@/components/ui/badge";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Separator } from "@/components/ui/separator";
import { buttonVariants } from "@/components/ui/button";
import { LinkedinMark } from "@/components/linkedin-mark";
import { SiteFooter } from "@/components/site-footer";
import { SiteHeader } from "@/components/site-header";
import {
  bring,
  certifications,
  education,
  experience,
  goals,
  profile,
  skillGroups,
  tanIntelligence,
  workGroups,
} from "@/lib/profile";
import { assetPath, cn } from "@/lib/utils";

export default function Home() {
  return (
    <div id="top" className="flex min-h-full flex-1 flex-col">
      <SiteHeader />
      <main className="flex-1">
        <Hero />
        <Experience />
        <Work />
        <TanIntelligence />
        <Goals />
        <Skills />
        <EducationCerts />
        <Contact />
      </main>
      <SiteFooter />
    </div>
  );
}

function Hero() {
  return (
    <section className="relative overflow-hidden">
      <div className="pointer-events-none absolute inset-0">
        <div className="absolute -top-32 right-0 h-96 w-96 rounded-full bg-cyan-400/12 blur-3xl" />
        <div className="absolute bottom-0 left-1/4 h-72 w-72 rounded-full bg-amber-400/8 blur-3xl" />
      </div>
      <div className="mx-auto grid max-w-6xl gap-10 px-4 py-16 sm:px-6 lg:grid-cols-[1.15fr_0.85fr] lg:py-24">
        <div className="relative">
          <p className="mb-5 inline-flex items-center gap-2 rounded-full border border-cyan-400/25 bg-cyan-400/8 px-3 py-1 text-xs font-medium tracking-wide text-cyan-200 uppercase">
            <Sparkles className="size-3.5" />
            {profile.kicker}
          </p>
          <h1 className="font-heading text-4xl leading-[1.05] tracking-tight text-zinc-50 sm:text-5xl lg:text-6xl">
            {profile.name}
          </h1>
          <p className="mt-5 max-w-xl text-lg text-zinc-300 sm:text-xl">
            {profile.headline}
          </p>
          <p className="mt-4 max-w-xl text-base leading-relaxed text-zinc-400">
            {profile.summary}
          </p>
          <p className="mt-4 flex flex-wrap items-center gap-x-2 gap-y-1 text-sm text-zinc-400">
            <MapPin className="size-4 text-cyan-300" />
            <span>{profile.location}</span>
            <span className="text-zinc-600">·</span>
            <span>{profile.onsite}</span>
          </p>
          <div className="mt-8 flex flex-wrap items-center gap-3">
            <a
              href={profile.resumeHref}
              target="_blank"
              rel="noreferrer"
              className={cn(buttonVariants({ size: "lg" }), "h-11 px-4 text-sm")}
            >
              <FileText data-icon="inline-start" />
              View resume
            </a>
            <a
              href={profile.linkedin.href}
              target="_blank"
              rel="noreferrer"
              className={cn(
                buttonVariants({ variant: "outline", size: "lg" }),
                "h-11 border-white/15 bg-white/4 px-4 text-sm text-zinc-100"
              )}
            >
              <LinkedinMark className="size-4" />
              LinkedIn
            </a>
            <a
              href={profile.guideHref}
              target="_blank"
              rel="noreferrer"
              className={cn(
                buttonVariants({ variant: "outline", size: "lg" }),
                "h-11 border-white/15 bg-white/4 px-4 text-sm text-zinc-100"
              )}
            >
              <FileText data-icon="inline-start" />
              Interview guide
            </a>
          </div>
        </div>
        <div className="relative">
          <div className="overflow-hidden rounded-2xl ring-1 ring-cyan-300/20 shadow-[0_0_80px_-24px_rgba(34,211,238,0.55)]">
            <Image
              src={assetPath("/work/ai-agentic-orchestration.jpg")}
              alt="Generative AI multi-agent orchestration dashboard with planner, researcher, and executor agents"
              width={1600}
              height={900}
              priority
              className="h-full w-full object-cover"
            />
          </div>
          <p className="mt-3 text-xs tracking-wide text-zinc-500 uppercase">
            Agentic systems · not a headshot
          </p>
        </div>
      </div>
      <div className="mx-auto grid max-w-6xl gap-3 px-4 pb-16 sm:grid-cols-2 sm:px-6 lg:grid-cols-5">
        {bring.map((item) => (
          <Card key={item.title} className="border-0 bg-[#101c26] ring-cyan-400/12">
            <CardHeader className="gap-2">
              <CardTitle className="text-sm tracking-wide text-cyan-100 uppercase">
                {item.title}
              </CardTitle>
            </CardHeader>
            <CardContent>
              <p className="text-sm leading-relaxed text-zinc-400">{item.copy}</p>
            </CardContent>
          </Card>
        ))}
      </div>
    </section>
  );
}

function Experience() {
  return (
    <section id="experience" className="scroll-mt-28 border-t border-white/8">
      <div className="mx-auto max-w-6xl px-4 py-16 sm:px-6">
        <SectionKicker>Experience</SectionKicker>
        <h2 className="font-heading mt-3 text-3xl tracking-tight text-zinc-50">
          Roles
        </h2>
        <div className="mt-8 space-y-6">
          {experience.map((role) => (
            <Card
              key={`${role.title}-${role.dates}`}
              className="border-0 bg-[#101c26] ring-cyan-400/15"
            >
              <CardHeader className="gap-3">
                <div className="flex flex-wrap items-start justify-between gap-3">
                  <div>
                    <CardTitle className="font-heading text-2xl text-zinc-50">
                      {role.title}
                    </CardTitle>
                    <CardDescription className="mt-1 text-base text-cyan-200/90">
                      {role.href ? (
                        <a
                          href={role.href}
                          className="underline-offset-4 hover:underline"
                          target="_blank"
                          rel="noreferrer"
                        >
                          {role.company}
                        </a>
                      ) : (
                        role.company
                      )}
                    </CardDescription>
                  </div>
                  <Badge
                    variant="outline"
                    className="border-cyan-400/30 bg-cyan-400/8 text-cyan-100"
                  >
                    {role.dates}
                  </Badge>
                </div>
                <p className="text-sm text-zinc-400">{role.location}</p>
              </CardHeader>
              <CardContent className="space-y-4">
                <p className="text-zinc-300">{role.summary}</p>
                <ul className="space-y-3 text-zinc-300">
                  {role.bullets.map((bullet) => (
                    <li key={bullet} className="flex gap-3">
                      <span className="mt-2 size-1.5 shrink-0 rounded-full bg-cyan-300" />
                      <span>{bullet}</span>
                    </li>
                  ))}
                </ul>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>
    </section>
  );
}

function Work() {
  return (
    <section id="work" className="scroll-mt-28 border-t border-white/8">
      <div className="mx-auto max-w-6xl px-4 py-16 sm:px-6">
        <SectionKicker>Featured work</SectionKicker>
        <h2 className="font-heading mt-3 max-w-2xl text-3xl tracking-tight text-zinc-50">
          Agentic systems, RAG, vision, and edge inference
        </h2>
        <p className="mt-3 max-w-2xl text-zinc-400">
          Production GenAI and computer-vision work from the Retailetics stack,
          plus the in-store products those systems ship inside. Not extra
          employers.
        </p>
        {workGroups.map((group) => (
          <div key={group.title} className="mt-12">
            <h3 className="font-heading text-xl tracking-tight text-zinc-50">
              {group.title}
            </h3>
            <p className="mt-2 max-w-2xl text-sm text-zinc-400">
              {group.intro}
            </p>
            <div className="mt-6 grid gap-6 md:grid-cols-2">
              {group.items.map((item) => (
                <article
                  key={item.slug}
                  className="overflow-hidden rounded-2xl bg-[#101c26] ring-1 ring-white/8"
                >
                  <Image
                    src={assetPath(item.image)}
                    alt={item.title}
                    width={1600}
                    height={900}
                    className="aspect-video w-full object-cover"
                  />
                  <div className="space-y-3 p-5">
                    <Badge
                      variant="outline"
                      className="border-amber-300/25 bg-amber-300/8 text-amber-100"
                    >
                      {item.tag}
                    </Badge>
                    <h3 className="font-heading text-xl text-zinc-50">
                      {item.title}
                    </h3>
                    <p className="text-sm leading-relaxed text-zinc-400">
                      {item.copy}
                    </p>
                  </div>
                </article>
              ))}
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}

function TanIntelligence() {
  return (
    <section id="tan" className="scroll-mt-28 border-t border-white/8">
      <div className="mx-auto max-w-6xl px-4 py-16 sm:px-6">
        <SectionKicker>Independent venture</SectionKicker>
        <h2 className="font-heading mt-3 text-3xl tracking-tight text-zinc-50">
          {tanIntelligence.company}
        </h2>
        <p className="mt-3 max-w-2xl text-zinc-400">
          {tanIntelligence.intro}
        </p>
        <div className="mt-10 grid gap-8 lg:grid-cols-[0.95fr_1.05fr] lg:items-center">
          <div className="overflow-hidden rounded-2xl ring-1 ring-white/10">
            <Image
              src={assetPath(tanIntelligence.image)}
              alt="Concept UI for an AI forex trading indicator on a dark terminal"
              width={1600}
              height={900}
              className="aspect-video w-full object-cover"
            />
          </div>
          <Card className="border-0 bg-[#101c26] ring-amber-300/15">
            <CardHeader className="gap-3">
              <div className="flex flex-wrap items-center gap-2">
                <Badge
                  variant="outline"
                  className="border-amber-300/30 bg-amber-300/8 text-amber-100"
                >
                  {tanIntelligence.tag}
                </Badge>
                <Badge
                  variant="secondary"
                  className="bg-white/6 text-zinc-200"
                >
                  {tanIntelligence.role}
                </Badge>
              </div>
              <CardTitle className="font-heading text-2xl text-zinc-50">
                {tanIntelligence.title}
              </CardTitle>
            </CardHeader>
            <CardContent className="space-y-4 text-zinc-300">
              <p>{tanIntelligence.summary}</p>
              {tanIntelligence.body.map((paragraph) => (
                <p key={paragraph} className="text-zinc-400">
                  {paragraph}
                </p>
              ))}
            </CardContent>
          </Card>
        </div>
      </div>
    </section>
  );
}

function Goals() {
  return (
    <section id="goals" className="scroll-mt-28 border-t border-white/8">
      <div className="mx-auto max-w-6xl px-4 py-16 sm:px-6">
        <SectionKicker>Goals</SectionKicker>
        <h2 className="font-heading mt-3 text-3xl tracking-tight text-zinc-50">
          Where the work is pointed
        </h2>
        <div className="mt-10 grid gap-6 lg:grid-cols-2">
          <Card className="border-0 bg-[#101c26] ring-cyan-400/15">
            <CardHeader>
              <p className="text-xs font-medium tracking-[0.18em] text-cyan-300/90 uppercase">
                Short-term
              </p>
              <CardTitle className="font-heading text-xl text-zinc-50">
                {goals.shortTerm.title}
              </CardTitle>
            </CardHeader>
            <CardContent className="space-y-4 text-zinc-300">
              <p>{goals.shortTerm.ai}</p>
              <p className="text-zinc-400">{goals.shortTerm.ml}</p>
            </CardContent>
          </Card>
          <Card className="border-0 bg-[#101c26] ring-amber-300/15">
            <CardHeader>
              <p className="text-xs font-medium tracking-[0.18em] text-amber-200/90 uppercase">
                Long-term
              </p>
              <CardTitle className="font-heading text-xl text-zinc-50">
                {goals.longTerm.title}
              </CardTitle>
            </CardHeader>
            <CardContent className="text-zinc-300">
              <p>{goals.longTerm.copy}</p>
            </CardContent>
          </Card>
        </div>
      </div>
    </section>
  );
}

function Skills() {
  return (
    <section id="skills" className="scroll-mt-28 border-t border-white/8">
      <div className="mx-auto max-w-6xl px-4 py-16 sm:px-6">
        <SectionKicker>Skills</SectionKicker>
        <h2 className="font-heading mt-3 text-3xl tracking-tight text-zinc-50">
          How the work actually ships
        </h2>
        <div className="mt-10 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {skillGroups.map((group) => (
            <Card key={group.title} className="border-0 bg-[#101c26] ring-white/8">
              <CardHeader>
                <CardTitle className="text-cyan-100">{group.title}</CardTitle>
              </CardHeader>
              <CardContent className="flex flex-wrap gap-2">
                {group.items.map((item) => (
                  <Badge
                    key={item}
                    variant="secondary"
                    className="bg-white/6 text-zinc-200"
                  >
                    {item}
                  </Badge>
                ))}
              </CardContent>
            </Card>
          ))}
        </div>
      </div>
    </section>
  );
}

function EducationCerts() {
  return (
    <section id="education" className="scroll-mt-28 border-t border-white/8">
      <div className="mx-auto grid max-w-6xl gap-10 px-4 py-16 sm:px-6 lg:grid-cols-2">
        <div>
          <SectionKicker>Education</SectionKicker>
          <h2 className="font-heading mt-3 text-3xl tracking-tight text-zinc-50">
            {education.degree}
          </h2>
          <p className="mt-3 text-lg text-zinc-300">{education.school}</p>
        </div>
        <div>
          <SectionKicker>Certifications</SectionKicker>
          <ul className="mt-6 space-y-4">
            {certifications.map((cert, index) => (
              <li key={cert.name}>
                {index > 0 ? <Separator className="mb-4 bg-white/8" /> : null}
                <p className="font-medium text-zinc-100">{cert.name}</p>
                <p className="text-sm text-zinc-400">{cert.issuer}</p>
              </li>
            ))}
          </ul>
        </div>
      </div>
    </section>
  );
}

function Contact() {
  return (
    <section id="contact" className="scroll-mt-28 border-t border-white/8">
      <div className="mx-auto max-w-6xl px-4 py-16 sm:px-6">
        <SectionKicker>Contact</SectionKicker>
          <h2 className="font-heading mt-3 text-3xl tracking-tight text-zinc-50">
          Based in Bengaluru
        </h2>
        <p className="mt-3 max-w-xl text-zinc-400">
          Current location {profile.location}. Also {profile.onsite}. Email,
          both phone numbers, and LinkedIn are on this page.
        </p>
        <div className="mt-8 flex flex-wrap gap-3">
          <a
            href={`mailto:${profile.email}`}
            className={cn(buttonVariants({ size: "lg" }), "h-11 px-4")}
          >
            <Mail data-icon="inline-start" />
            {profile.email}
          </a>
          {profile.phones.map((phone) => (
            <a
              key={phone.display}
              href={phone.href}
              className={cn(
                buttonVariants({ variant: "outline", size: "lg" }),
                "h-11 border-white/15 bg-white/4 px-4 text-zinc-100"
              )}
            >
              <Phone data-icon="inline-start" />
              {phone.display}
            </a>
          ))}
          <a
            href={profile.linkedin.href}
            target="_blank"
            rel="noreferrer"
            className={cn(
              buttonVariants({ variant: "outline", size: "lg" }),
              "h-11 border-white/15 bg-white/4 px-4 text-zinc-100"
            )}
          >
            <LinkedinMark className="size-4" />
            LinkedIn
          </a>
          <a
            href={profile.resumeHref}
            target="_blank"
            rel="noreferrer"
            className={cn(
              buttonVariants({ variant: "outline", size: "lg" }),
              "h-11 border-white/15 bg-white/4 px-4 text-zinc-100"
            )}
          >
            <FileText data-icon="inline-start" />
            {profile.resumeLabel}
          </a>
          <a
            href={profile.guideHref}
            target="_blank"
            rel="noreferrer"
            className={cn(
              buttonVariants({ variant: "outline", size: "lg" }),
              "h-11 border-white/15 bg-white/4 px-4 text-zinc-100"
            )}
          >
            <FileText data-icon="inline-start" />
            {profile.guideLabel}
          </a>
        </div>
        <div className="mt-8 space-y-2 text-sm text-zinc-500">
          <p>
            <a
              href={profile.company.href}
              className="text-cyan-200/80 underline-offset-4 hover:underline"
              target="_blank"
              rel="noreferrer"
            >
              {profile.company.legalName}
            </a>
            <ArrowUpRight className="ml-1 inline size-3.5" />
          </p>
        </div>
      </div>
    </section>
  );
}

function SectionKicker({ children }: { children: ReactNode }) {
  return (
    <p className="text-xs font-medium tracking-[0.22em] text-cyan-300/90 uppercase">
      {children}
    </p>
  );
}
